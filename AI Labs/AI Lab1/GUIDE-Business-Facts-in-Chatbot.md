# Giving Chatbots Business Information: A Complete Guide

## The Problem: LLM Hallucination

Without providing your business facts, the LLM **makes things up**:

```
❌ Customer: "How much is a mountain bike?"
❌ Bot: "Mountain bikes are $20/day" (But you charge $25!)
❌ Bot: "We also rent kayaks" (But you don't offer that!)
```

## The Solution: Embed Facts in System Prompt

Put your actual data in the **system message**, and instruct the LLM to use only that information.

```
✅ Customer: "How much is a mountain bike?"
✅ Bot: "Mountain bikes are $25/day with a free helmet included!"
✅ Customer: "Do you rent kayaks?"
✅ Bot: "I don't have that information. Please call us at (808) 555-1234"
```

---

## Step-by-Step: How to Do It

### Step 1: Create a Dictionary of Your Facts

```python
business_facts = {
    "name": "Aloha Bikes",
    "location": "Waikiki",
    "phone": "(808) 555-1234",
    "hours": "8 AM - 6 PM daily",
    "cruiser_price": "$15/day",
    "mountain_bike_price": "$25/day",
    "electric_bike_price": "$45/day",
    "helmet": "Free with rental",
    "deposit": "$50 (refunded)",
    "group_discount": "10% for 5+ people"
}
```

**What to include:**
- ✅ Prices (most important!)
- ✅ Hours & availability
- ✅ Contact info
- ✅ Policies & terms
- ✅ Available products/services
- ✅ Special offers
- ❌ Things you don't offer (don't mention them)

### Step 2: Format Facts into System Prompt

**Option A: Simple string embedding**
```python
system_prompt = f"""You are a helpful assistant for {business_facts['name']}.

PRICING:
- Cruiser: {business_facts['cruiser_price']}
- Mountain Bike: {business_facts['mountain_bike_price']}

POLICIES:
- Helmet: {business_facts['helmet']}
- Deposit: {business_facts['deposit']}

Answer questions using ONLY this information."""
```

**Option B: JSON format (cleanest)**
```python
import json

system_prompt = f"""You are a helpful assistant for Aloha Bikes.

Business Data:
{json.dumps(business_facts, indent=2)}

Answer customer questions using ONLY the data above.
Never make up prices or policies."""
```

**Option C: Formatted text (most readable)**
```python
system_prompt = """You are a helpful assistant for Aloha Bikes.

BUSINESS FACTS:
━━━━━━━━━━━━━━━━━━━━━━━━━
📍 Location: Waikiki
⏰ Hours: 8 AM - 6 PM daily
📞 Phone: (808) 555-1234

🚲 BIKE RENTALS:
  • Cruiser: $15/day
  • Mountain Bike: $25/day
  • Electric Bike: $45/day
  
📋 POLICIES:
  • Helmet: FREE (required)
  • Deposit: $50 (refunded)
  • Group discount: 10% for 5+
━━━━━━━━━━━━━━━━━━━━━━━━━

INSTRUCTIONS:
✓ Answer using ONLY these facts
✓ Be friendly and helpful
✗ NEVER make up information
✗ If asked about services not listed, say "I don't have that info, call us"""
```

### Step 3: Use in Your Chatbot

```python
messages = [
    {"role": "system", "content": system_prompt},  # Your facts go here
    {"role": "user", "content": "How much is a mountain bike?"}
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages
)

print(response.choices[0].message.content)
# Output: "Mountain bikes are $25/day! Free helmet included. 🚲"
```

### Step 4: Keep Facts in Every Turn

Always include the system prompt with your facts in every conversation:

```python
messages = [
    {"role": "system", "content": system_prompt},  # Always first!
    {"role": "user", "content": "What are your hours?"},
    {"role": "assistant", "content": "We're open 8 AM - 6 PM daily!"},
    {"role": "user", "content": "Do you offer insurance?"}  # Still uses facts
]
```

---

## Three Real Examples

### Example 1: Bike Rental Shop
```python
facts = {
    "name": "Aloha Bikes",
    "cruiser": "$15/day",
    "mountain": "$25/day",
    "electric": "$45/day",
    "helmet": "Free",
    "group_10plus": "10% off"
}
```

### Example 2: Coffee Shop
```python
facts = {
    "name": "Manoa Cafe",
    "location": "University of Hawaii",
    "hours": "6 AM - 9 PM",
    "coffee": "$3.50",
    "latte": "$5.00",
    "pastry": "$4.50",
    "wifi": "Free with purchase",
    "seating": "Limited"
}
```

### Example 3: Hotel
```python
facts = {
    "name": "Waikiki Resort",
    "phone": "(808) 555-6789",
    "rooms_per_night": "$120-$200",
    "check_in": "3 PM",
    "check_out": "11 AM",
    "amenities": ["Pool", "Gym", "Free WiFi", "Restaurant"],
    "parking": "$15/day",
    "pets": "Not allowed"
}
```

---

## Common Mistakes & How to Fix Them

| Mistake | Problem | Fix |
|---------|---------|-----|
| Facts not in system prompt | LLM ignores them | Add to system message |
| System prompt removed mid-conversation | LLM forgets facts | Keep it in every turn |
| Facts incomplete | LLM makes up missing info | Update dictionary |
| Facts unclear | LLM misinterprets | Use clear formatting |
| "Please make something up" in prompt | LLM hallucInates anyway | Remove that instruction |

---

## Testing Your System Prompt

**Test 1: Basic Facts**
- Q: "What's your phone number?"
- A: Should match exactly ✅

**Test 2: Prices**
- Q: "How much is X?"
- A: Should match exactly ✅

**Test 3: Out of Scope**
- Q: "Do you offer services_we_don't_have?"
- A: "I don't have that information" ✅

**Test 4: Policy Questions**
- Q: "What's your cancellation policy?"
- A: Either states it correctly OR "I don't have that info" ✅

---

## Files Provided

| File | Purpose |
|------|---------|
| `Chatbot.5.with-facts.py` | Full example with auto-formatting |
| `Chatbot.5.simple-facts.py` | Minimal example (easiest to modify) |
| `Chatbot.5.quickstart.py` | Copy & paste starter template |
| `Chatbot.5.concepts.py` | Reference guide with all patterns |

---

## Pro Tips

1. **Keep facts in a separate file or database**
   ```python
   import json
   with open("business_facts.json") as f:
       facts = json.load(f)
   ```

2. **Update facts easily**
   ```python
   facts["coffee_price"] = "$4.00"  # Update easily in code
   ```

3. **Use environment variables for sensitive info**
   ```python
   facts["owner_email"] = os.environ.get("OWNER_EMAIL")
   ```

4. **Add versioning to track changes**
   ```python
   facts["_version"] = "1.2 (Updated Nov 2024)"
   ```

5. **Monitor what the LLM says**
   ```python
   # Log responses to verify accuracy
   with open("chatbot_log.txt", "a") as f:
       f.write(f"Q: {user_question}\nA: {bot_answer}\n\n")
   ```

---

## Summary

**To prevent chatbot hallucination:**

1. 📋 Create a **dictionary** of your business facts
2. 📝 Format them into the **system prompt**
3. 📌 **Keep the system prompt** in every conversation
4. ✅ **Test** to ensure the bot uses your facts
5. 🔄 **Update** facts when things change

**Result:** A chatbot that answers from your data, not imagination! 🚀
