import ollama

print("Starting LLM test...")

response = ollama.chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": "Explain artificial intelligence in one sentence."
        }
    ]
)

print("\nRaw response:")
print(response)

print("\nModel answer:")
print(response["message"]["content"])