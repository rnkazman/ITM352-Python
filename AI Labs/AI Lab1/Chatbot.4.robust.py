import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI, APIError, RateLimitError, APIConnectionError, APIStatusError

load_dotenv()

# ============================================================================
# 1. VALIDATE API KEY
# ============================================================================
def validate_api_key():
    """Ensure API key exists and is not empty."""
    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        print("❌ ERROR: OPENROUTER_API_KEY not found!")
        print("   Please create a .env file with: OPENROUTER_API_KEY=your_key_here")
        print("   Or set the environment variable directly.")
        sys.exit(1)
    return api_key


# ============================================================================
# 2. INITIALIZE CLIENT WITH ERROR HANDLING
# ============================================================================
def initialize_client(api_key):
    """Create OpenAI client for OpenRouter."""
    try:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            timeout=10.0,  # 10 second timeout for requests
        )
        return client
    except Exception as e:
        print(f"❌ ERROR: Failed to initialize client: {e}")
        sys.exit(1)


# ============================================================================
# 3. TEST API CONNECTION
# ============================================================================
def test_api_connection(client):
    """Quick test to verify API is reachable."""
    try:
        # Try a minimal request to verify connectivity
        response = client.chat.completions.create(
            model="openrouter/free",  # Free/fast model for testing
            messages=[{"role": "system", "content": "Say 'ok'"}],
            max_tokens=5,
            temperature=0,
        )
        print("✅ API connection successful!")
        return True
    except APIConnectionError as e:
        print(f"❌ ERROR: Cannot reach OpenRouter API. Check your internet connection.")
        print(f"   Details: {e}")
        return False
    except APIStatusError as e:
        if e.status_code == 429:
            print(f"❌ ERROR: Rate limited (quota exceeded). Try again later.")
        elif e.status_code == 503:
            print(f"❌ ERROR: OpenRouter service unavailable (maintenance?). Try again later.")
        else:
            print(f"❌ ERROR: API returned status {e.status_code}: {e.message}")
        return False
    except Exception as e:
        print(f"❌ ERROR: Unexpected connection error: {e}")
        return False


# ============================================================================
# 4. HANDLE CONVERSATION WITH RETRY LOGIC
# ============================================================================
def call_llm_with_retry(client, messages, max_retries=3, backoff_seconds=2):
    """
    Call LLM with exponential backoff retry logic.
    
    - Handles rate limits with pause-and-retry
    - Handles temporary service unavailability
    - Respects free-tier quotas
    """
    model = "openrouter/free"
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=500,
            )
            return response.choices[0].message.content
            
        except RateLimitError as e:
            remaining = backoff_seconds * (2 ** attempt)  # Exponential backoff
            if attempt < max_retries - 1:
                print(f"⚠️  Rate limit hit. Waiting {remaining}s before retry...")
                time.sleep(remaining)
            else:
                print(f"❌ ERROR: Free-tier quota exhausted. Please wait before continuing.")
                return None
                
        except APIStatusError as e:
            if e.status_code == 503:  # Service unavailable
                remaining = backoff_seconds * (2 ** attempt)
                if attempt < max_retries - 1:
                    print(f"⚠️  Service temporarily unavailable. Waiting {remaining}s...")
                    time.sleep(remaining)
                else:
                    print(f"❌ ERROR: OpenRouter service is down. Try again later.")
                    return None
            else:
                print(f"❌ ERROR: API error {e.status_code}: {e.message}")
                return None
                
        except APIConnectionError as e:
            print(f"❌ ERROR: Network connection lost. Check your internet connection.")
            return None
            
        except APIError as e:
            print(f"❌ ERROR: Unexpected API error: {e}")
            return None
    
    return None


# ============================================================================
# 5. MANAGE CONVERSATION HISTORY (PREVENT UNBOUNDED GROWTH)
# ============================================================================
class ConversationManager:
    """
    Manages conversation history with safeguards against:
    - Unbounded token growth
    - Context window overflow
    """
    
    def __init__(self, system_context, max_turns=20):
        self.system_message = {"role": "system", "content": system_context}
        self.max_turns = max_turns  # Keep only last N user/assistant pairs
        self.messages = [self.system_message]
        self.turn_count = 0
    
    def add_user_message(self, text):
        """Add user message and trim history if needed."""
        self.messages.append({"role": "user", "content": text})
        self.turn_count += 1
        self._trim_history()
    
    def add_assistant_message(self, text):
        """Add assistant response."""
        self.messages.append({"role": "assistant", "content": text})
    
    def _trim_history(self):
        """
        Keep system message + last N conversation turns.
        Each turn = 1 user message + 1 assistant response.
        """
        if len(self.messages) > 1 + (self.max_turns * 2):
            # Keep system message + last N turns
            self.messages = [self.system_message] + self.messages[-(self.max_turns * 2):]
            print(f"📝 [History trimmed to last {self.max_turns} turns to manage memory]")
    
    def get_messages(self):
        """Return messages ready to send to API."""
        return self.messages
    
    def get_stats(self):
        """Return conversation stats for debugging."""
        return {
            "total_messages": len(self.messages),
            "turn_count": self.turn_count,
            "max_turns": self.max_turns,
        }


# ============================================================================
# 6. MAIN CHATBOT
# ============================================================================
def main():
    print("🤖 Initializing robust chatbot...\n")
    
    # Step 1: Validate API key
    api_key = validate_api_key()
    
    # Step 2: Initialize client
    client = initialize_client(api_key)
    
    # Step 3: Test connection
    if not test_api_connection(client):
        print("\n⚠️  Continuing anyway (may fail on first message)...\n")
    
    # Step 4: Get system context
    system_context = input("\nEnter system context (e.g., 'You are a helpful assistant'): ").strip()
    if not system_context:
        system_context = "You are a helpful AI assistant."
    
    # Step 5: Initialize conversation manager
    conversation = ConversationManager(system_context, max_turns=20)
    
    print('\n✅ Ready! Type "quit", "bye", or "exit" to end.\n')
    
    # Step 6: Main loop
    while True:
        user_text = input("You: ").strip()
        
        if user_text.lower() in ("quit", "bye", "exit"):
            print("Bot: Thanks for chatting! Goodbye!")
            break
        
        if not user_text:
            continue
        
        # Add user message to history
        conversation.add_user_message(user_text)
        
        # Call LLM with retry logic
        print("Bot: ", end="", flush=True)
        reply = call_llm_with_retry(client, conversation.get_messages())
        
        if reply is None:
            print("[No response - request failed]")
            # Remove failed user message so user can retry
            conversation.messages.pop()
            conversation.turn_count -= 1
        else:
            print(reply)
            conversation.add_assistant_message(reply)
        
        # Optionally show stats (uncomment for debugging)
        # stats = conversation.get_stats()
        # print(f"  [Messages: {stats['total_messages']}, Turns: {stats['turn_count']}]")


if __name__ == "__main__":
    main()
