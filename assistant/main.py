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

print(f"{bot.name} is online")
print("type 'exit' to shut down.\n")

while True:
    user_message = (input("you: "))
    
    if user_message.lower().strip() == "exit":
        print(f"{bot.name}: Goodbye!")
        break

    response = bot.respond(user_message)
    print(F"{bot.name}: {response}")