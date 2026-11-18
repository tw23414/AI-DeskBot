
# Changelog


## v0.7.0 – Initial Installer Demo

### Added
- Created the first AI-DeskBot Windows installer using Inno Setup.
- Added an installer script (`installer/installer.iss`).
- Installer creates an AI-DeskBot installation directory.
- Installer copies the required assistant, brain, memory and personality files.
- Added a Start Menu shortcut.

### Improved
- Excluded personal memory data from installer packages.
- Excluded unnecessary Python cache files.
- Added installer build output to `.gitignore`.

### Notes
- Generated the first installer executable: `AI-DeskBot-Setup-v0.7.0.exe`.
- Installer compilation successful.
- Full installation testing remains outstanding because Windows Application Control blocked execution.


## v0.6.0 – Smarter Long-Term Memory

### Added
- Automatic detection of ordinary memories.
- Separate ordinary and long-term memory types.
- Automatic 30-day expiry for ordinary memories.
- Automatic removal of expired memories.
- Duplicate memory prevention.
- Relevant memory retrieval.
- Improved AI accuracy when discussing saved memories.

### Improved
- AI-DeskBot uses relevant memories when answering questions.
- AI-DeskBot avoids inventing unsupported personal information.
- Memory persistence across restarts.


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
