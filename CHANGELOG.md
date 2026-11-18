
# Changelog

## v0.5.0 - The AI Brain

- Integrated Ollama as the local AI runtime.
- Downloaded and configured the Llama 3.2 1B model.
- Created a separate AI brain module.
- Connected Python to Ollama using the Requests library.
- Added natural language conversations.
- Integrated AI-DeskBot's existing personality into AI responses.
- Added conversation context during active sessions.
- Preserved the persistent memory system.
- Tested memory commands alongside the AI brain.
- Added connection error handling.
- Tested recovery after restarting Ollama.

## v0.4.0 - Memory Improvements

- Added numbered memory lists.
- Added the `forget` command to delete individual memories.
- Added the `clear memory` command with confirmation.
- Added protection against saving empty memories.
- Improved memory handling and validation.
- Tested memory saving and loading across restarts.

## v0.3.0 - Persistent Memory

- Created a separate memory system.
- Added persistent JSON memory storage.
- Added remember command.
- Added recall command.
- Connected memory to the main assistant.
- Tested memory persistence across restarts.

## v0.2.0 - Personality System

- Created a separate personality module.
- Added AI-DeskBot's name, description and tone.
- Added a personality introduction.
- Connected the personality module to the main assistant.

## v0.1.0 - First Working Prototype

- Created the basic AI-DeskBot class.
- Added simple text-based conversations.
- Added basic responses to greetings and questions.
- Added an exit command.
- Set up Git version control.
