"""commands.py - Interprets recognized text and performs the matching action."""

import datetime
import urllib.parse
import webbrowser

from speaker import speak
from listener import listen

EXIT_WORDS = {"exit", "quit", "stop", "bye", "goodbye"}
SEARCH_TRIGGERS = ("search for", "search about", "search on", "search", "google", "look up")


def greet() -> None:
    speak("Hello! I am your voice assistant. How can I help you today?")


def tell_time() -> None:
    now = datetime.datetime.now()
    speak(f"The current time is {now.strftime('%I:%M %p')}.")


def tell_date() -> None:
    now = datetime.datetime.now()
    speak(f"Today is {now.strftime('%A, %d %B %Y')}.")


def extract_topic(text: str) -> str:
    """Return whatever the user said after the search trigger phrase."""
    for trigger in SEARCH_TRIGGERS:
        if trigger in text:
            return text.split(trigger, 1)[1].strip()
    return ""


def web_search(text: str) -> None:
    topic = extract_topic(text)

    # User said only "search" with no topic: ask for one
    if not topic:
        speak("What would you like me to search for?")
        topic = listen()
        if not topic:
            speak("I couldn't get a topic, so I cancelled the search.")
            return

    speak(f"Searching the web for {topic}.")
    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(topic)
    webbrowser.open(url)


def handle_command(text: str) -> bool:
    """
    Run the action that matches the text.
    Returns False when the assistant should stop, otherwise True.
    """
    words = set(text.split())

    # Search is checked first so "search time zones" searches instead of telling time
    if any(trigger in text for trigger in SEARCH_TRIGGERS):
        web_search(text)
        return True

    if words & EXIT_WORDS:
        speak("Goodbye! Have a great day.")
        return False

    handled = False

    if "hello" in words or "hi" in words or "hey" in words:
        greet()
        handled = True

    if "time" in words:
        tell_time()
        handled = True

    if "date" in words or "today" in words or "day" in words:
        tell_date()
        handled = True

    if not handled:
        speak("Sorry, I can only greet you, tell the time and date, or search the web. Please try again.")

    return True