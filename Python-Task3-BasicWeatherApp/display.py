def show_banner():
    """Print the app header."""
    print("=" * 40)
    print("   Basic Weather App")
    print("=" * 40)


def display_weather(data):
    """Format and display the weather data."""
    temp_c = data["main"]["temp"]
    temp_f = temp_c * 9 / 5 + 32
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"].title()
    wind_speed = data["wind"]["speed"]
    city = data["name"]

    print("\n" + "=" * 40)
    print(f"   Weather for: {city}")
    print("=" * 40)
    print(f"  Temperature:  {temp_c:.1f}°C / {temp_f:.1f}°F")
    print(f"  Humidity:     {humidity}%")
    print(f"  Condition:    {condition}")
    print(f"  Wind Speed:   {wind_speed:.1f} m/s")
    print("=" * 40)   