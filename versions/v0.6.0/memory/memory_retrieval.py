
import re


class MemoryRetrieval:

    STOP_WORDS = {
        "i", "me", "my", "do", "does", "did",
        "what", "when", "where", "why", "how",
        "is", "are", "am", "the", "a", "an",
        "to", "of", "in", "on", "and", "or",
        "you", "your", "it", "this", "that",
        "like", "enjoy", "love", "have", "has"
    }

    def find_relevant(self, message, memories):
        message_words = set(
            re.findall(r"\b[a-z0-9']+\b", message.lower())
        )

        message_words -= self.STOP_WORDS

        relevant_memories = []

        for memory in memories:
            memory_words = set(
                re.findall(
                    r"\b[a-z0-9']+\b",
                    memory["information"].lower()
                )
            )

            memory_words -= self.STOP_WORDS

            if message_words.intersection(memory_words):
                relevant_memories.append(memory)

        return relevant_memories


retrieval = MemoryRetrieval()
