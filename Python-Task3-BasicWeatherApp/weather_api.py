import sys
import requests
from config import API_KEY, BASE_URL, TIMEOUT


def get_location():
    """Prompt user for city name or ZIP code with validation."""
    while True:
        location = input("Enter city name or ZIP code: ").strip()
        if not location:
            print("Error: Input cannot be empty. Please try again.")
            continue
        return location


def fetch_weather(location):
    """Call OpenWeatherMap API and return parsed JSON data."""
    params = {
        "q": location,
        "units": "metric",
        "appid": API_KEY,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please check your internet connection.")
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the weather service.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: Network request failed — {e}")
        sys.exit(1)

    if response.status_code == 401:
        print("Error: Invalid API key. Please check your OpenWeatherMap API key.")
        sys.exit(1)
    elif response.status_code == 404:
        print(f"Error: Location '{location}' not found. Please check the spelling.")
        sys.exit(1)
    elif response.status_code == 429:
        print("Error: API rate limit exceeded. Please try again after 60 seconds.")
        sys.exit(1)
    elif response.status_code != 200:
        print(f"Error: Unexpected API response (status {response.status_code}).")
        sys.exit(1)

    return response.json()   