import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)
MODEL = "openrouter/free"

System_context = input("Enter system context (e.g., 'You are an assistant for Aloha Bikes, You are at barista a Manoa cafe, etc.'): ").strip()

messages = [{"role": "system", "content": System_context}]

print('Your custom chatbot. Type "quit" or "bye" to exit.')

while True:
    user_text = input("You: ").strip()
    if user_text.lower() in ("quit", "bye"):
        print("Bot: Thanks for using the chatbot!")
        break
    if not user_text:
        continue

    messages.append({"role": "user", "content": user_text})
    response = client.chat.completions.create(model=MODEL, messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print(f"Bot: {reply}")
