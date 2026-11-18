
import json
import os
from datetime import datetime, timedelta


class Memory:
    def __init__(self):
        folder = os.path.dirname(__file__)
        self.file_path = os.path.join(folder, "memories.json")
        self.memories = self.load_memories()

    def load_memories(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)

                if data and isinstance(data[0], str):
                    data = [
                        {
                            "id": number,
                            "information": item,
                            "type": "long-term",
                            "created": datetime.now().isoformat(),
                            "expires": None
                        }
                        for number, item in enumerate(data, start=1)
                    ]
                    self.memories = data
                    self.save_memories()

                return data

        return []

    def save_memories(self):
        with open(self.file_path, "w") as file:
            json.dump(self.memories, file, indent=4)

    def remember(self, information, memory_type="long-term"):
        information = information.strip()

        if not information:
            return False

        for item in self.memories:
            if item["information"].lower() == information.lower():
                return False

        created = datetime.now()

        if memory_type == "ordinary":
            expires = (created + timedelta(days=30)).isoformat()
        else:
            expires = None

        memory_id = max(
            [item["id"] for item in self.memories],
            default=0
        ) + 1

        self.memories.append({
            "id": memory_id,
            "information": information,
            "type": memory_type,
            "created": created.isoformat(),
            "expires": expires
        })

        self.save_memories()
        return True

    def remove_expired(self):
        now = datetime.now()
        original_count = len(self.memories)

        self.memories = [
            item for item in self.memories
            if item["expires"] is None
            or datetime.fromisoformat(item["expires"]) > now
        ]

        if len(self.memories) != original_count:
            self.save_memories()

    def recall(self):
        self.remove_expired()
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
