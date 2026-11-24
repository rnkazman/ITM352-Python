import os

from dotenv import load_dotenv
from openai import OpenAI

from ex2 import INFO, MENU, MODEL, build_system_prompt

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

messages = [{"role": "system", "content": build_system_prompt(MENU, INFO)}]

print('Mānoa Bytes Café chatbot. Type "quit" or "bye" to exit.')

while True:
    user_text = input("You: ").strip()
    if user_text.lower() in ("quit", "bye"):
        print("Bot: Mahalo for visiting Mānoa Bytes Café!")
        break
    if not user_text:
        continue

    messages.append({"role": "user", "content": user_text})
    response = client.chat.completions.create(model=MODEL, messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print(f"Bot: {reply}")
    print(f"[history: {len(messages)} messages]")