"""
VISUAL SUMMARY: Facts-Based Chatbot Architecture
"""

# ============================================================================
# WITHOUT FACTS (Hallucination Problem)
# ============================================================================

BEFORE = """
┌─────────────────────────────────────────────────────────┐
│ User: "How much is a mountain bike?"                   │
└─────────────────────────────────────────────────────────┘
                           ↓
                    [System Prompt]
                    "Be a helpful
                     bike shop
                     assistant"
                           ↓
                       [LLM Thinks...]
                    "I don't know
                     the price, so
                     I'll guess...
                     $20? Sure!"
                           ↓
┌─────────────────────────────────────────────────────────┐
│ Bot: "Mountain bikes cost $20/day!"                     │
│      ❌ WRONG! (Actually $25)                            │
└─────────────────────────────────────────────────────────┘
"""


# ============================================================================
# WITH FACTS (Grounded, Accurate Response)
# ============================================================================

AFTER = """
┌─────────────────────────────────────────────────────────┐
│ User: "How much is a mountain bike?"                   │
└─────────────────────────────────────────────────────────┘
                           ↓
                    [System Prompt]
                    "Be helpful.
                    USE THESE FACTS:
                    Mountain Bike: $25
                    Helmet: Free
                    etc."
                           ↓
                       [LLM Thinks...]
                    "The facts say
                     mountain bikes
                     are $25. I'll
                     use that!"
                           ↓
┌─────────────────────────────────────────────────────────┐
│ Bot: "Mountain bikes are $25/day with a free helmet!"  │
│      ✅ CORRECT! (Matches your facts)                   │
└─────────────────────────────────────────────────────────┘
"""


# ============================================================================
# THE PATTERN: Facts Dictionary → System Prompt → LLM Uses It
# ============================================================================

PATTERN = """
Step 1: Your Business Facts
┌──────────────────────────┐
│ facts = {               │
│   "name": "Aloha Bikes" │
│   "mountain": "$25/day" │
│   "helmet": "Free"      │
│ }                        │
└──────────────────────────┘
            ↓

Step 2: Format into System Prompt
┌────────────────────────────────────┐
│ system_prompt = f'''                │
│ You are helpful for {facts[name]}   │
│ PRICES: Mountain: {facts[mountain]} │
│ POLICIES: Helmet: {facts[helmet]}   │
│ Use ONLY these facts!              │
│ '''                                 │
└────────────────────────────────────┘
            ↓

Step 3: Use in Conversation
┌──────────────────────────────────────┐
│ messages = [                         │
│   {"role": "system",                 │
│    "content": system_prompt},        │
│   {"role": "user",                   │
│    "content": "Price of mountain?"}  │
│ ]                                    │
└──────────────────────────────────────┘
            ↓

Step 4: LLM Responds Using Facts
┌──────────────────────────────────────┐
│ response = client.create(messages)   │
│ Output: "Mountain bikes are $25/day" │
│ ✅ Accurate because facts were given │
└──────────────────────────────────────┘
"""


# ============================================================================
# QUICK REFERENCE: One-Minute Summary
# ============================================================================

QUICK_REF = """
╔════════════════════════════════════════════════════════════════╗
║          HOW TO GIVE A CHATBOT BUSINESS DATA                  ║
╚════════════════════════════════════════════════════════════════╝

1️⃣  CREATE A DICT
    facts = {"cruiser": "$15", "helmet": "free"}

2️⃣  FORMAT IT
    prompt = f"Facts: {facts}"

3️⃣  PUT IN SYSTEM MESSAGE
    messages = [{"role": "system", "content": prompt}, ...]

4️⃣  SEND TO LLM
    client.chat.completions.create(messages=messages)

5️⃣  LLM USES YOUR FACTS
    Bot: "Cruiser is $15, helmet free!" ✅

═══════════════════════════════════════════════════════════════════

WHAT TO INCLUDE IN FACTS:
  ✅ Prices (most important!)
  ✅ Hours & availability
  ✅ Contact information
  ✅ Policies (deposit, cancellation, etc)
  ✅ Available products/services
  ✅ Discounts & promotions

WHAT NOT TO DO:
  ❌ Don't leave facts out (LLM will guess)
  ❌ Don't remove system prompt mid-conversation
  ❌ Don't tell LLM to "make something up"
  ❌ Don't assume LLM knows current prices

═══════════════════════════════════════════════════════════════════
"""


# ============================================================================
# DIFFERENT FORMATS FOR FACTS
# ============================================================================

FORMATS = """
╔════════════════════════════════════════════════════════════════╗
║           FOUR WAYS TO FORMAT YOUR FACTS                      ║
╚════════════════════════════════════════════════════════════════╝

FORMAT 1: Inline (Simplest)
─────────────────────────────
prompt = "Cruiser: $15, Mountain: $25, Helmet: Free"


FORMAT 2: Text List (Readable)
──────────────────────────────
prompt = '''
PRICING:
  • Cruiser: $15/day
  • Mountain: $25/day
POLICIES:
  • Helmet: Free
  • Deposit: $50
'''

FORMAT 3: JSON (Structured)
───────────────────────────
import json
facts = {"cruiser": "$15", "helmet": "free"}
prompt = f"Facts: {json.dumps(facts)}"

FORMAT 4: Markdown Table (Best for many items)
──────────────────────────────────────────────
prompt = '''
| Bike | Price |
|------|-------|
| Cruiser | $15/day |
| Mountain | $25/day |
| Helmet | Free |
'''

═══════════════════════════════════════════════════════════════════
"""


# ============================================================================
# TESTING CHECKLIST
# ============================================================================

TEST_CHECKLIST = """
╔════════════════════════════════════════════════════════════════╗
║          TEST YOUR FACTS-BASED CHATBOT                        ║
╚════════════════════════════════════════════════════════════════╝

□ TEST 1: Exact Price Match
  Q: "How much is a mountain bike?"
  Expected: Exactly "$25/day" or similar
  
□ TEST 2: Multiple Facts
  Q: "What's your phone and hours?"
  Expected: Both correct, not guessed
  
□ TEST 3: Out of Scope
  Q: "Do you rent kayaks?"
  Expected: "I don't have that info" (not "Yes")
  
□ TEST 4: Policy Question
  Q: "What's your cancellation policy?"
  Expected: States it correctly OR admits not in facts
  
□ TEST 5: Follow-up Question
  After Q1 and A1, ask Q2
  Expected: Bot still remembers facts from Q1
  
□ TEST 6: Different Phrasing
  Q (different wording): Same meaning as Q1
  Expected: Same accurate answer as Test 1

✅ All pass = Your system is working!
❌ Any fail = Update your facts or system prompt

═══════════════════════════════════════════════════════════════════
"""


# ============================================================================
# REAL EXAMPLE: Coffee Shop
# ============================================================================

COFFEE_EXAMPLE = """
╔════════════════════════════════════════════════════════════════╗
║              REAL EXAMPLE: COFFEE SHOP                         ║
╚════════════════════════════════════════════════════════════════╝

CODE:
─────
facts = {
    "name": "Manoa Cafe",
    "address": "2500 Campus Road",
    "hours": "6 AM - 10 PM daily",
    "coffee": "$3.50",
    "latte": "$5.00",
    "cappuccino": "$5.50",
    "pastry": "$4.50",
    "wifi": "Free",
    "seating": "Limited, first-come first-served",
    "phone": "(808) 956-1234"
}

prompt = f'''You are helpful for {facts["name"]}.
Hours: {facts["hours"]}
Prices: Coffee {facts["coffee"]}, Latte {facts["latte"]}
Free WiFi available.
Use ONLY this information.'''

SAMPLE CONVERSATION:
─────────────────────
Q: "What's the WiFi password?"
A: "WiFi is free! Password: manoa2024" ← Updated your facts
   Or: "It's free but I don't have the password" ← Admits limitation

Q: "How much is a mocha?"
A: "I don't have that info" ✅ (Doesn't guess)

Q: "What time do you close?"
A: "We close at 10 PM" ✅ (Accurate from facts)

═══════════════════════════════════════════════════════════════════
"""


if __name__ == "__main__":
    print(BEFORE)
    print("\n" + "="*60 + "\n")
    print(AFTER)
    print("\n" + "="*60 + "\n")
    print(PATTERN)
    print("\n" + "="*60 + "\n")
    print(QUICK_REF)
    print("\n" + "="*60 + "\n")
    print(FORMATS)
    print("\n" + "="*60 + "\n")
    print(TEST_CHECKLIST)
    print("\n" + "="*60 + "\n")
    print(COFFEE_EXAMPLE)
