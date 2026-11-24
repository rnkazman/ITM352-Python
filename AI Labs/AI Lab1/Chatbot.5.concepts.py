"""
KEY CONCEPTS: How to prevent LLM hallucination

The Problem:
  Without business facts, the LLM makes things up:
  "Mountain bikes are $12/day" (WRONG - you say $25)
  "We have surfboards" (WRONG - you don't)

The Solution:
  Put your facts in the SYSTEM PROMPT - the LLM will use them.
"""

# ============================================================================
# CONCEPT 1: Dictionary of Facts
# ============================================================================
business_facts = {
    "name": "Aloha Bikes",
    "location": "Waikiki",
    "hours": "8 AM - 6 PM",
    "prices": {
        "cruiser": "$15/day",
        "mountain_bike": "$25/day"
    }
}
# Use this dict in your prompt to ensure accuracy!


# ============================================================================
# CONCEPT 2: Embedding Facts in System Prompt
# ============================================================================

# BAD - no facts, LLM will hallucinate
bad_prompt = """You are a helpful assistant for a bike rental shop.
Answer customer questions."""

# GOOD - facts included, LLM uses them
good_prompt = """You are a helpful assistant for Aloha Bikes.

BUSINESS FACTS:
- Location: Waikiki
- Hours: 8 AM - 6 PM
- Mountain Bike: $25/day
- Helmet: Free

Answer questions ONLY using these facts."""

# BEST - dynamic, using your data
def create_prompt(facts):
    facts_list = "\n".join([f"- {k}: {v}" for k, v in facts.items()])
    return f"""You are a helpful assistant for {facts['name']}.

FACTS:
{facts_list}

Answer using ONLY these facts."""


# ============================================================================
# CONCEPT 3: Three Ways to Structure Facts
# ============================================================================

# Method 1: Simple string
facts_string = "Hours: 8-6, Mountain Bike: $25, Helmet: Free"

# Method 2: Formatted text (best for readability)
facts_formatted = """
PRICING:
  - Cruiser: $15/day
  - Mountain Bike: $25/day
  - Electric Bike: $45/day
POLICIES:
  - Helmet: Free
  - Deposit: $50 (refunded)
"""

# Method 3: JSON (best for structured data)
import json
facts_json = json.dumps({
    "prices": {"cruiser": "$15/day", "mountain_bike": "$25/day"},
    "policies": {"helmet": "Free", "deposit": "$50"}
})

# All three work! Pick what's clearest for your data.


# ============================================================================
# CONCEPT 4: What to Put in Facts
# ============================================================================
complete_facts = {
    # Contact & Location
    "business_name": "Aloha Bikes",
    "address": "123 Main St, Waikiki",
    "phone": "(808) 555-1234",
    "email": "info@alohabikes.com",
    
    # Hours & Availability
    "hours": "8 AM - 6 PM daily",
    "closed_days": "Christmas, New Year's",
    
    # Pricing (THE MOST IMPORTANT!)
    "bike_prices": {
        "cruiser": "$15/day",
        "mountain": "$25/day",
        "electric": "$45/day"
    },
    "helmet_cost": "Free",
    "insurance_cost": "$5/day (optional)",
    "deposit": "$50 (refunded)",
    
    # Policies
    "helmet_required": True,
    "max_rental_days": 7,
    "group_discount": "10% for 5+ people",
    
    # Services/Products
    "available_bikes": ["Cruiser", "Mountain Bike", "Electric Bike", "Kids Bike"],
    "accessories": ["Lock", "Water Bottle Holder", "Phone Mount"],
    
    # Popular Info
    "best_routes": ["Diamond Head - 5 miles", "Waikiki Beach - 3 miles"],
    "best_season": "April-October"
}


# ============================================================================
# CONCEPT 5: Instructions for the LLM
# ============================================================================
complete_system_prompt = """You are a friendly customer service chatbot for Aloha Bikes.

BUSINESS FACTS:
- Name: Aloha Bikes
- Location: Waikiki
- Hours: 8 AM - 6 PM daily (closed Christmas & New Year's)
- Phone: (808) 555-1234
- Cruiser: $15/day
- Mountain Bike: $25/day
- Electric Bike: $45/day
- Helmet: FREE
- Deposit: $50 (refunded after rental)

INSTRUCTIONS:
✓ Answer using ONLY the facts above
✓ Be friendly and helpful
✓ Keep responses short (2-3 sentences)
✓ If asked something not in facts, say "I don't have that info, call us at (808) 555-1234"
✗ NEVER make up prices or policies
✗ NEVER invent services we don't offer"""


# ============================================================================
# CONCEPT 6: Format Examples
# ============================================================================

# Example 1: Simple inline
prompt_1 = """You are Aloha Bikes assistant. Prices: Cruiser $15, Mountain $25, Electric $45. Helmet free. 
Answer questions using ONLY this info."""

# Example 2: Bulleted list
prompt_2 = """You are Aloha Bikes assistant.

FACTS:
• Cruiser: $15/day
• Mountain Bike: $25/day
• Electric Bike: $45/day
• Helmet: Free
• Deposit: $50 (refunded)

RULES: Answer using ONLY these facts."""

# Example 3: Markdown table
prompt_3 = """You are Aloha Bikes assistant.

| Item | Price |
|------|-------|
| Cruiser | $15/day |
| Mountain Bike | $25/day |
| Electric Bike | $45/day |
| Helmet | Free |

Answer customer questions using this table."""

# Example 4: JSON
prompt_4 = """You are Aloha Bikes assistant. Here's our data:

```json
{
  "bike_rentals": {
    "cruiser": "$15/day",
    "mountain_bike": "$25/day",
    "electric_bike": "$45/day"
  },
  "included": ["Free Helmet", "Free Lock"],
  "deposit": "$50 (refunded)"
}
```

Use ONLY this information."""


print("""
SUMMARY: How to Stop LLM Hallucination
======================================

1. CREATE A DICTIONARY of your business facts
   facts = {"name": "Aloha Bikes", "cruiser": "$15/day", ...}

2. FORMAT IT into your system prompt
   system_prompt = f"Facts: {json.dumps(facts)}"

3. GIVE INSTRUCTIONS to use only those facts
   "Answer using ONLY the facts provided. Never make up information."

4. USE THAT SYSTEM PROMPT in every conversation
   messages = [{"role": "system", "content": system_prompt}, ...]

5. TEST IT by asking questions about prices and policies
   - Answers should match your facts exactly
   - If LLM says "I don't have that info", that's good!

RESULT:
  ✓ Accurate business information
  ✓ No made-up prices or policies
  ✓ Customers get the right info
  ✓ Fewer customer complaints!
""")
