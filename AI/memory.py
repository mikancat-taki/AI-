class MemoryModule:
    def __init__(self):
        self.history = []
        self.emotion = "😊"
    def add_user_message(self, msg):
        self.history.append(("user", msg))
    def add_bot_message(self, msg):
        self.history.append(("bot", msg))
    def get_emotion_state(self):
        # ユーザーの単語に応じて感情を変える
        if any(word in self.history[-1][1] for word in ["怒", "ムカ", "嫌"]):
            self.emotion = "😠"
        elif any(word in self.history[-1][1] for word in ["嬉", "楽", "好き"]):
            self.emotion = "😄"
        return self.emotion
