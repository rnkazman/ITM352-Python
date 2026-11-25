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
user_message = "My name is Rick"    
messages = [
    {"role": "user", "content": user_message}
]

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": user_message}]
)
saved_response = response.choices[0].message.content 
print("First response")
print(response.choices[0].message.content)

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is my name?"}]
)
print("Second response")
print(response.choices[0].message.content)

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": user_message}, 
              {"role": "assistant", "content": saved_response},
              {"role": "user", "content": "What is my name?"}]
)
print("Third response, with memory...")
print(response.choices[0].message.content)
