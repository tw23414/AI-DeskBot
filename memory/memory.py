import json
import os


class Memory:
    def __init__(self):
        self.file_path = "memory/memories.json"
        self.memories = self.load_memories()

    def load_memories(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)

        return []

    def save_memories(self):
        with open(self.file_path, "w") as file:
            json.dump(self.memories, file, indent=4)

    def remember(self, information):
        self.memories.append(information)
        self.save_memories()

    def recall(self):
        return self.memories


memory = Memory()