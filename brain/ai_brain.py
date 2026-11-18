
import requests


class AIBrain:
    def __init__(self, model="llama3.2:1b"):
        self.model = model
        self.api_url = "http://localhost:11434/api/chat"
        self.conversation = []

    def think(self, message, personality, memories=None):
        self.conversation.append({
            "role": "user",
            "content": message
        })

        memory_context = "\n\nSaved memories:\n"

        if memories:
            for item in memories:
                memory_context += (
                    f"- {item['information']} "
                    f"({item['type']})\n"
                )
        else:
            memory_context += "No saved memories.\n"

        system_prompt = (
            f"You are {personality.name}. "
            f"{personality.description} "
            f"Your speaking style is: {personality.tone}. "

            "IMPORTANT RULES: "
            "Keep replies to 1-2 short sentences. "
            "Be friendly and natural. "
            "Only state personal facts that are directly supported "
            "by saved memories or things the user explicitly said. "

            "Do not invent examples, details or explanations about "
            "the user's hobbies or interests. "

            "Knowing that the user likes drawing does NOT mean you know "
            "what they draw. "

            "Knowing that the user enjoys making games does NOT mean "
            "you know their skill level or experience. "

            "Never turn a guess into a fact. "
            "If information is missing, clearly say you do not know. "
            "Never pretend to remember something that was not saved. "

            f"{memory_context}"
        )

        messages = [
            {
                "role": "system",
                "content": system_prompt
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
