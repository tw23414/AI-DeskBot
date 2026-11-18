
import requests


class AIBrain:
    def __init__(self, model="llama3.2:1b"):
        self.model = model
        self.api_url = "http://localhost:11434/api/chat"
        self.conversation = []

    def think(self, message, personality):
        self.conversation.append({
            "role": "user",
            "content": message
        })

        messages = [
            {
                "role": "system",
                "content": (
                    f"You are {personality.name}. "
                    f"{personality.description} "
                    f"Your speaking style is: {personality.tone}. "
                    "Be helpful, curious and friendly."
                )
            }
        ] + self.conversation

        try:
            response = requests.post(
                self.api_url,
                json={
                    "model": self.model,
                    "messages": messages,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()
            answer = response.json()["message"]["content"]

            self.conversation.append({
                "role": "assistant",
                "content": answer
            })

            return answer

        except requests.RequestException as error:
            self.conversation.pop()
            return f"I'm having trouble connecting to my AI brain: {error}"


brain = AIBrain()
