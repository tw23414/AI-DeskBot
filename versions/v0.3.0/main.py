
from personality.personality import personality
from memory.memory import memory


class AIDeskBot:
    def __init__(self):
        self.name = "AI-DeskBot"

    def respond(self, message):
        message = message.lower().strip()

        if message in ["hello", "hi", "hey"]:
            return "Hello! I'm AI-DeskBot. Nice to meet you."

        elif "your name" in message:
            return f"My name is {self.name}."

        elif "how are you" in message:
            return "I'm doing well! What would you like to do?"

        else:
            return "I'm still learning. I don't know how to respond to that yet."


bot = AIDeskBot()

print(f"{bot.name} is online!")
print(personality.introduce())
print("Memory system loaded!")
print("Type 'exit' to shut down.\n")

while True:
    user_message = input("You: ")

    if user_message.lower().strip() == "exit":
        print(f"{bot.name}: Goodbye!")
        break

    elif user_message.lower().startswith("remember "):
        information = user_message[9:]
        memory.remember(information)
        print(f"{bot.name}: I'll remember that.")

    elif user_message.lower().strip() == "recall":
        saved_memories = memory.recall()

        if saved_memories:
            print(f"{bot.name}: Here's what I remember:")
            for item in saved_memories:
                print(f"- {item}")
        else:
            print(f"{bot.name}: I don't have any memories yet.")

    else:
        response = bot.respond(user_message)
        print(f"{bot.name}: {response}")
