from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler
model, tokenizer = load("mlx-community/Qwen2.5-3B-Instruct-4bit")

sampler = make_sampler(temp=0.7, top_p=0.9, top_k=40)

history = []

while True:
    user = input("You: ")
    
    history.append({"role": "user", "content": user})

    prompt = tokenizer.apply_chat_template(
        history,
        tokenize=False,
        add_generation_prompt=True
    )

    response = generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=2000,
        sampler=sampler
    )

    print("Bot:", response)

    history.append({"role": "assistant", "content": response})