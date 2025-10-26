class EmotionModule:
    def __init__(self):
        self.state = {"happy": 0.5, "sad": 0.5}

    def update(self, text):
        if "!" in text or "love" in text:
            self.state["happy"] += 0.1
        if "bad" in text or "hate" in text:
            self.state["sad"] += 0.1
        for k in self.state:
            self.state[k] = max(0, min(1, self.state[k]))

    def summary(self):
        return f"😊 {self.state['happy']:.2f} 😢 {self.state['sad']:.2f}"
