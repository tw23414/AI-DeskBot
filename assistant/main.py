
from personality.personality import personality
from memory.memory import memory
from memory.memory_detector import detector
from memory.memory_retrieval import retrieval
from brain.ai_brain import brain


class AIDeskBot:
    def __init__(self):
        self.name = "AI-DeskBot"

    def respond(self, message):
        relevant_memories = retrieval.find_relevant(
            message,
            memory.recall()
        )

        return brain.think(
            message,
            personality,
            relevant_memories
        )


bot = AIDeskBot()

print(f"{bot.name} is online!")
print(personality.introduce())
print("Memory system loaded!")
print("AI brain loaded!")
print("Automatic memory detection loaded!")
print("Relevant memory retrieval loaded!")
print("Type 'exit' to shut down.\n")

while True:
    user_message = input("You: ")
    command = user_message.lower().strip()

    if command == "exit":
        print(f"{bot.name}: Goodbye!")
        break

    elif command == "remember" or command.startswith("remember "):
        information = user_message[9:].strip()

        if memory.remember(information, "long-term"):
            print(f"{bot.name}: I'll remember that.")
        else:
            print(f"{bot.name}: I couldn't save that. It may be empty or already saved.")

    elif command == "recall":
        saved_memories = memory.recall()

        if saved_memories:
            print(f"{bot.name}: Here's what I remember:")

            for number, item in enumerate(saved_memories, start=1):
                print(
                    f"{number}. {item['information']} "
                    f"({item['type']})"
                )
        else:
            print(f"{bot.name}: I don't have any memories yet.")

    elif command.startswith("forget "):
        try:
            number = int(command[7:])

            if memory.forget(number):
                print(f"{bot.name}: Memory {number} forgotten.")
            else:
                print(f"{bot.name}: I couldn't find memory {number}.")

        except ValueError:
            print(f"{bot.name}: Please give me a valid memory number.")

    elif command == "clear memory":
        confirmation = input(
            f"{bot.name}: Are you sure you want to delete all memories? (yes/no): "
        )

        if confirmation.lower().strip() == "yes":
            memory.clear()
            print(f"{bot.name}: All memories cleared.")
        else:
            print(f"{bot.name}: Memory clearing cancelled.")

    else:
        detected_memory = detector.detect(user_message)

        if detected_memory:
            if memory.remember(detected_memory, "ordinary"):
                print(f"{bot.name}: I'll keep that in mind!")
            else:
                print(f"{bot.name}: I already have that saved!")

        response = bot.respond(user_message)
        print(f"{bot.name}: {response}")
