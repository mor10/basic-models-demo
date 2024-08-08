from tools.owm import get_weather_by_location


def main():
    # Display a welcome message
    print("Welcome to the Basic Terminal App!")

    # Ask for the user's location
    question = "Please enter your location to get the current weather:"
    print(question)

    # Allow the user to type in an answer
    location = input("Your location: ")

    # Get the weather by location
    weather_info = get_weather_by_location(location)

    # Display the weather information
    print(f"The current weather in {location} is: {weather_info}")


if __name__ == "__main__":
    main()
