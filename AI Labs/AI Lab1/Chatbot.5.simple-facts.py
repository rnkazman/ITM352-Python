"""
SIMPLE EXAMPLE: Embedding business facts in system prompt
"""
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
# YOUR BUSINESS DATA
# ============================================================================
facts = {
    "name": "Aloha Bikes",
    "location": "Waikiki",
    "hours": "8 AM - 6 PM daily",
    "cruiser_price": "$15/day",
    "mountain_bike_price": "$25/day",
    "electric_bike_price": "$45/day",
    "helmet": "Free",
    "group_discount": "10% off for 5+ people",
    "phone": "(808) 555-1234"
}

# ============================================================================
# CREATE SYSTEM PROMPT WITH FACTS
# ============================================================================
# Option 1: Simple string
system_prompt_simple = f"""You are a helpful assistant for {facts['name']}.

Business Facts:
- Location: {facts['location']}
- Hours: {facts['hours']}
- Cruiser: {facts['cruiser_price']}
- Mountain Bike: {facts['mountain_bike_price']}
- Electric Bike: {facts['electric_bike_price']}
- Helmet: {facts['helmet']}
- Group Discount: {facts['group_discount']}
- Phone: {facts['phone']}

Answer questions using ONLY these facts. If asked about something not listed, say you don't have that information."""

# Option 2: Using JSON format (even cleaner)
import json

system_prompt_json = f"""You are a helpful assistant for {facts['name']}.

Here is the business information in JSON format:
{json.dumps(facts, indent=2)}

Answer customer questions using ONLY this information. Never make up prices or policies."""

# ============================================================================
# USE IT IN A CONVERSATION
# ============================================================================
messages = [
    {"role": "system", "content": system_prompt_simple},
    {"role": "user", "content": "How much does a mountain bike cost and are helmets free?"}
]

response = client.chat.completions.create(model=MODEL, messages=messages)
print("Q: How much does a mountain bike cost and are helmets free?")
print(f"A: {response.choices[0].message.content}\n")

# ============================================================================
# TRY ASKING SOMETHING NOT IN THE FACTS
# ============================================================================
messages = [
    {"role": "system", "content": system_prompt_simple},
    {"role": "user", "content": "Do you offer surfboard rentals?"}
]

response = client.chat.completions.create(model=MODEL, messages=messages)
print("Q: Do you offer surfboard rentals?")
print(f"A: {response.choices[0].message.content}\n")
