
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

    elif user_message.lower().strip() == "remember" or user_message.lower().startswith("remember "):
        information = user_message[9:]

        if memory.remember(information):
            print(f"{bot.name}: I'll remember that.")
        else:
            print(f"{bot.name}: I can't save an empty memory.")

    elif user_message.lower().strip() == "recall":
        saved_memories = memory.recall()

        if saved_memories:
            print(f"{bot.name}: Here's what I remember:")
            for number, item in enumerate(saved_memories, start=1):
                print(f"{number}. {item}")
        else:
            print(f"{bot.name}: I don't have any memories yet.")

    elif user_message.lower().startswith("forget "):
        try:
            number = int(user_message[7:])
            if memory.forget(number):
                print(f"{bot.name}: Memory {number} forgotten.")
            else:
                print(f"{bot.name}: I couldn't find memory {number}.")
        except ValueError:
            print(f"{bot.name}: Please give me a valid memory number.")

    elif user_message.lower().strip() == "clear memory":
        confirmation = input(
            f"{bot.name}: Are you sure you want to delete all memories? (yes/no): "
        )

        if confirmation.lower().strip() == "yes":
            memory.clear()
            print(f"{bot.name}: All memories cleared.")
        else:
            print(f"{bot.name}: Memory clearing cancelled.")

    else:
        response = bot.respond(user_message)
        print(f"{bot.name}: {response}")