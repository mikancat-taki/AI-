import json, os

class MemoryModule:
    def __init__(self, path="memory.json"):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({"history": []}, f)
        self.load()

    def load(self):
        with open(self.path, "r") as f:
            self.data = json.load(f)

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f)

    def remember(self, text):
        self.data["history"].append(text)
        if len(self.data["history"]) > 50:
            self.data["history"] = self.data["history"][-50:]
        self.save()

    def recall(self):
        return " ".join(self.data["history"][-5:])
