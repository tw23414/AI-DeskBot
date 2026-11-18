
class MemoryDetector:

    def detect(self, message):
        message = message.strip()

        if not message:
            return None

        useful_phrases = [
            "i like ",
            "i love ",
            "i enjoy ",
            "my favourite ",
            "my favorite ",
            "i prefer ",
            "i am interested in ",
            "i'm interested in "
        ]

        lowered_message = message.lower()

        for phrase in useful_phrases:
            if lowered_message.startswith(phrase):
                return message

        return None


detector = MemoryDetector()
