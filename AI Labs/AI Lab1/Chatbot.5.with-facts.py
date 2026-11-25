import os
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
# BUSINESS FACTS DICTIONARY
# ============================================================================
# This is YOUR data - prices, hours, policies, locations, etc.
# The LLM will use this instead of making things up.
business_facts = {
    "business_name": "Aloha Bikes",
    "location": "Waikiki, Honolulu, Hawaii",
    "hours": {
        "monday_to_sunday": "8:00 AM - 6:00 PM",
        "holidays": "Closed on Christmas, Thanksgiving, and New Year's Day"
    },
    "bike_rentals": {
        "cruiser": "$15/day",
        "mountain_bike": "$25/day",
        "electric_bike": "$45/day",
        "kids_bike": "$10/day"
    },
    "helmet": "Free with any rental",
    "deposit": "$50 credit card hold (refunded)",
    "insurance": "$5/day for damage coverage (optional)",
    "phone": "(808) 555-1234",
    "email": "info@alohbikes.com",
    "popular_routes": {
        "diamond_head": "5 miles, moderate difficulty, 1.5 hours",
        "waikiki_beach": "3 miles, easy, 45 minutes",
        "manoa_falls": "7 miles, challenging, 2 hours"
    },
    "group_discounts": "10% off for groups of 5+ people",
    "helmet_required": True,
    "max_rental_period": "7 days",
    "best_months": "April-October (dry season)"
}


# ============================================================================
# FUNCTION: Format facts into system prompt
# ============================================================================
def create_system_prompt(business_data):
    """
    Takes a business dictionary and formats it into a system prompt
    that the LLM will follow.
    """
    # Build the facts section
    facts_text = "BUSINESS FACTS (Use this information to answer questions):\n"
    facts_text += "-" * 50 + "\n"
    
    for key, value in business_data.items():
        if isinstance(value, dict):
            # Handle nested dictionaries (like hours, prices)
            facts_text += f"{key.upper().replace('_', ' ')}:\n"
            for sub_key, sub_value in value.items():
                facts_text += f"  • {sub_key.replace('_', ' ').title()}: {sub_value}\n"
        else:
            # Handle simple values
            facts_text += f"• {key.replace('_', ' ').title()}: {value}\n"
    
    facts_text += "-" * 50 + "\n"
    
    # Create the full system prompt
    system_prompt = f"""You are a friendly and helpful customer service assistant for Aloha Bikes.

{facts_text}

INSTRUCTIONS:
- Answer questions using ONLY the facts provided above. Never make up information.
- If asked about something not in the facts, politely say "I don't have that information" and offer to help with what you do know.
- Keep responses to 2-3 sentences unless more detail is requested.
- Be friendly and enthusiastic about Aloha Bikes and Hawaii.
- If a customer wants to know something not covered, suggest they call or email."""
    
    return system_prompt


# ============================================================================
# TEST 1: Show what the system prompt looks like
# ============================================================================
print("=" * 60)
print("SYSTEM PROMPT PREVIEW:")
print("=" * 60)
system_prompt = create_system_prompt(business_facts)
print(system_prompt)
print("\n")


# ============================================================================
# TEST 2: Run a chatbot conversation using the facts-based prompt
# ============================================================================
print("=" * 60)
print("CHATBOT CONVERSATION:")
print("=" * 60 + "\n")

# Start with the system prompt containing facts
messages = [
    {"role": "system", "content": system_prompt}
]

# Test questions - these should be answered from facts, not hallucination
test_questions = [
    "What are your hours?",
    "How much is a mountain bike rental?",
    "Do helmets cost extra?",
    "What's your best route for a beginner?",
    "Do you offer group discounts?",
    "When's the best time to visit Hawaii for biking?",
]

for question in test_questions:
    messages.append({"role": "user", "content": question})
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    
    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    
    print(f"Q: {question}")
    print(f"A: {answer}\n")


# ============================================================================
# TEST 3: Interactive chatbot (uncomment to use)
# ============================================================================
"""
print("=" * 60)
print("INTERACTIVE CHATBOT")
print("=" * 60)
print('Type "quit" to exit.\n')

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ("quit", "bye", "exit"):
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    
    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    
    print(f"Bot: {answer}\n")
"""
