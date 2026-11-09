"""main.py - Entry point for the Voice Assistant."""

from speaker import speak
from listener import listen
from commands import handle_command


def main() -> None:
    speak("Voice assistant activated. Say hello to begin, or say exit to quit.")
    running = True
    while running:
        text = listen()
        if text is None:       # not heard / not understood; listen again
            continue
        running = handle_command(text)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAssistant stopped by user.")
    except (OSError, AttributeError) as error:
        # OSError: no microphone found. AttributeError: PyAudio not installed.
        print(f"Microphone problem: {error}")
        print("Check that a microphone is connected and PyAudio is installed.")