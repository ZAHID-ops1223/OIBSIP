"""speaker.py - Text-to-speech helper using pyttsx3."""

import pyttsx3


def speak(text: str) -> None:
    """Print the text and speak it aloud."""
    print(f"Assistant: {text}")
    try:
        # A fresh engine per call avoids pyttsx3's "stops speaking after first
        # call" bug seen on some systems.
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)    # words per minute
        engine.setProperty("volume", 1.0)  # 0.0 to 1.0
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as error:
        # If audio output fails, the text is still printed above
        print(f"[TTS error: {error}]")


if __name__ == "__main__":
    speak("Text to speech is working correctly.")