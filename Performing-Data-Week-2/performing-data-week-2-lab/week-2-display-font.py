from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler

from dorothy import Dorothy

dot = Dorothy()

class MySketch():

    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        self.model, self.tokenizer = load("mlx-community/Qwen2.5-3B-Instruct-4bit")
        self.history = []
        self.sampler = make_sampler(temp=0.7, top_p=0.9, top_k=40)
        self.user_prompt = """
        write a script for the first scene of a film that is adapted from a comic book about two cats that live in a large shoe and fight crime
        Write a gritty noir opening scene for a film adapted from a comic book. Two anthropomorphic cats — seasoned street detectives — live in 
        a giant battered shoe in a rain-soaked city and fight crime. Open mid-action
        Format as a screenplay with short, punchy dialogue lines — no scene descriptions longer than one sentence
        The scene should open with the cats already in danger — something bigger than they expected has arrived at the shoe
        """
        self.history = [
            {"role": "system", "content": "You write terse, cinematic screenplays. Short lines. High tension. Noir atmosphere."},
            {"role": "user", "content": self.user_prompt}
        ]
        prompt = self.tokenizer.apply_chat_template(
            self.history,
            tokenize=False,
            add_generation_prompt=True
        )
        print("generating script")
        self.response = generate(
            self.model,
            self.tokenizer,
            prompt=prompt,
            max_tokens=2000,
            sampler=self.sampler
        )
        print("generated script", self.response)
        self.history.append({"role": "assistant", "content": self.response})
        self.ptr = 0
    
    def draw(self):
        dot.background(dot.white)
        dot.fill(dot.black)
        dot.text(self.response.split("\n")[self.ptr], 0, 0, 24)

        if dot.frames%200==0:
            self.ptr+=1
        
MySketch()
        