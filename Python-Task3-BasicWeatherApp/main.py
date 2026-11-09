from weather_api import get_location, fetch_weather
from display import show_banner, display_weather


def main():
    show_banner()
    location = get_location()
    data = fetch_weather(location)
    display_weather(data)


if __name__ == "__main__":
    main()   