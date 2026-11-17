import json
import os


class Memory:
    def __init__(self):
        folder = os.path.dirname(__file__)
        self.file_path = os.path.join(folder, "memories.json")
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
        information = information.strip()

        if information:
            self.memories.append(information)
            self.save_memories()
            return True

        return False

    def recall(self):
        return self.memories

    def forget(self, number):
        if 1 <= number <= len(self.memories):
            self.memories.pop(number - 1)
            self.save_memories()
            return True

        return False

    def clear(self):
        self.memories = []
        self.save_memories()


memory = Memory()