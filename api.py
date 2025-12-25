# mini-project, Dec 23, fetched an AI API using MegaLLM as a gateway + API key

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://ai.megallm.io/v1",
    api_key = os.getenv("MEGALLM_API_KEY")
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("Chat with AI (type 'quit' to exit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="openai-gpt-oss-20b",
        messages=messages
    )

    assistant_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_message})

    print(f"AI: {assistant_message}\n")

