"""listener.py - Captures voice from the microphone and converts it to text."""

import speech_recognition as sr
from speaker import speak

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1.0  # seconds of silence that ends a phrase


def listen():
    """
    Listen through the microphone and return the recognized text in lowercase.
    Returns None if nothing was heard or the speech was not understood
    (after asking the user to repeat).
    """
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        try:
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please say that again.")
            return None

    try:
        text = recognizer.recognize_google(audio, language="en-IN")
        print(f"You said: {text}")
        return text.lower().strip()
    except sr.UnknownValueError:
        # Speech was unclear / not understood
        speak("Sorry, I did not understand that. Could you please repeat?")
        return None
    except sr.RequestError:
        # No internet or the API is unreachable
        speak("I can't reach the speech service. Please check your internet connection.")
        return None


if __name__ == "__main__":
    result = listen()
    if result:
        speak(f"You said {result}")