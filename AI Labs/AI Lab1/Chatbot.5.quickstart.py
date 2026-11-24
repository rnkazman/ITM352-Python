"""
QUICK START: Copy & modify this for your business
"""
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent / ".env")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)
MODEL = "openrouter/free"

# ============================================================================
# STEP 1: Define your business facts
# ============================================================================
# EDIT THIS SECTION with your actual business data!
business_facts = {
    "business_name": "Aloha Bikes",
    "location": "Waikiki, Honolulu",
    "phone": "(808) 555-1234",
    "email": "info@alohabikes.com",
    "hours": {
        "weekday": "8:00 AM - 6:00 PM",
        "weekend": "8:00 AM - 7:00 PM",
        "closed": "Christmas, New Year's Day"
    },
    "rentals": {
        "cruiser": "$15/day",
        "mountain_bike": "$25/day",
        "electric_bike": "$45/day",
        "kids_bike": "$10/day"
    },
    "policies": {
        "helmet": "FREE with rental (required)",
        "deposit": "$50 credit card hold (refunded)",
        "insurance": "$5/day optional damage coverage",
        "max_days": "7 consecutive days"
    },
    "discounts": {
        "group_5plus": "10% off",
        "weekly": "5% off (5+ days)",
        "daily": "No daily discount"
    }
}


# ============================================================================
# STEP 2: Create a system prompt from your facts
# ============================================================================
def build_system_prompt(facts):
    """Convert your facts dict into a system prompt."""
    
    # Format the facts into readable text
    facts_text = "BUSINESS INFORMATION:\n"
    
    for section, data in facts.items():
        # Skip business_name, location (use them separately)
        if section in ["business_name", "location"]:
            continue
        
        section_title = section.replace("_", " ").upper()
        facts_text += f"\n{section_title}:\n"
        
        if isinstance(data, dict):
            for key, value in data.items():
                key_name = key.replace("_", " ").title()
                facts_text += f"  • {key_name}: {value}\n"
        else:
            facts_text += f"  • {data}\n"
    
    # Build complete system prompt
    prompt = f"""You are a friendly and professional customer service chatbot for {facts['business_name']}.
You are located in {facts['location']}.

{facts_text}

RESPONSE GUIDELINES:
1. Use ONLY the information provided above when answering questions
2. If asked about something not listed, respond: "I don't have that information. Please call us at {facts['phone']}"
3. Keep responses helpful, friendly, and brief (1-2 sentences)
4. Always encourage customers to visit or call for more details
5. Never invent prices, policies, or services not listed above
6. If a customer is upset, apologize and suggest they speak with management"""
    
    return prompt


# ============================================================================
# STEP 3: Use it in your chatbot
# ============================================================================
def ask_chatbot(question):
    """Ask a single question and get a response."""
    
    system_prompt = build_system_prompt(business_facts)
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7
    )
    
    return response.choices[0].message.content


# ============================================================================
# STEP 4: Run the chatbot
# ============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print(f"🚲 {business_facts['business_name']} Customer Support Bot")
    print("=" * 60 + "\n")
    
    # First, show the system prompt being used
    system_prompt = build_system_prompt(business_facts)
    print("SYSTEM PROMPT BEING USED:")
    print("-" * 60)
    print(system_prompt)
    print("-" * 60 + "\n")
    
    # Test with some example questions
    test_questions = [
        "What's your phone number?",
        "How much is a mountain bike?",
        "Are helmets free?",
        "Do you offer group discounts?",
        "What are your hours on Saturday?",
        "Do you rent scooters?",
        "What's the deposit?",
    ]
    
    print("EXAMPLE Q&A:\n")
    try:
        for question in test_questions:
            answer = ask_chatbot(question)
            print(f"Q: {question}")
            print(f"A: {answer}\n")
    except Exception as e:
        print(f"⚠️  API Error: {e}")
        print("\n💡 Note: If you see a rate limit error, you've hit the free quota.")
        print("   The system prompt above shows what WOULD be sent to the LLM.")
    
    # Interactive mode (uncomment to enable)
    """
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE - Type 'quit' to exit")
    print("=" * 60 + "\n")
    
    while True:
        user_question = input("You: ").strip()
        if user_question.lower() in ("quit", "bye", "exit"):
            print("Bot: Thank you for visiting Aloha Bikes! 🚲")
            break
        if not user_question:
            continue
        
        answer = ask_chatbot(user_question)
        print(f"Bot: {answer}\n")
    """
