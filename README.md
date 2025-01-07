# JARVIS - Voice Assistant

JARVIS is a voice-activated assistant that can perform various tasks such as opening websites, playing music, and fetching news. It uses speech recognition and text-to-speech technologies to interact with the user.

## Features

- Open websites like Google, Facebook, YouTube, and LinkedIn.
- Play music from a predefined music library.
- Fetch and read out the latest news headlines.
- Handle general queries using OpenAI.

## Requirements

- Python 3.x
- `speech_recognition` library
- `webbrowser` library
- `pyttsx3` library
- `requests` library
- `pygame` library
- `gtts` library
- `google-generativeai` library

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd "MEGA PROJECT (JARVIS)"
    ```
3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```sh
    python main.py
    ```
2. Say "Jarvis" to activate the assistant.
3. Give commands such as "open Google", "play [song name]", or "news".

## Code Overview

- [main.py](http://_vscodecontentref_/0): The main script that initializes and runs the voice assistant.
- `MusicLibrary.py`: Contains the music library with song names and their corresponding links.

## Example Commands

- "Open Google"
- "Open Facebook"
- "Open YouTube"
- "Open LinkedIn"
- "Play [song name]"
- "News"

## License

This project is licensed under the MIT License.