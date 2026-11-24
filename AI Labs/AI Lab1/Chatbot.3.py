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

messages = [
    {"role": "user", "content": "My name is Rick"}
]

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "My name is Rick"}]
)

saved_response = response.choices[0].message.content 
print(saved_response)

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is my name?"},
              {"role": "assistant", "content": saved_response}]
)
print(response.choices[0].message.content)
