import ollama

#pull model first 
# e.g. 
# ollama pull qwen2.5:0.5b

messages = []

while True:
    user = input("You: ")
    messages.append({"role": "user", "content": user})

    response = ollama.chat(
        model="qwen2.5:0.5b",
        messages=messages,
        options={
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 40,
            "repeat_penalty": 1.1
        }
    )

    reply = response["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print(f"Bot: {reply}")