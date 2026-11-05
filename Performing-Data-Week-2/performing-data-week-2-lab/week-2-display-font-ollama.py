import ollama

from dorothy import Dorothy

dot = Dorothy()

class MySketch():

    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        self.history = []
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
        print("generating script")
        self.response = ollama.chat(
            model="qwen2.5:0.5b",
            messages=self.history,
            options={
                "temperature": 0.7,
                "top_p": 0.9,
                "top_k": 40,
                "repeat_penalty": 1.1
            }
        )
        print("generated script", self.response)
        self.script = self.response.message.content
        self.history.append({"role": "assistant", "content": self.script})
        self.ptr = 0
    
    def draw(self):
        dot.background(dot.white)
        dot.fill(dot.black)
        dot.text(self.script.split("\n")[self.ptr], 0, 0, 24)

        if dot.frames%200==0:
            self.ptr+=1
        
MySketch()
        