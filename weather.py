from tools.owm import get_weather_by_location
from tools.get_location import get_location_string
from tools.analyze_weather import analyze_weather


def main():
    # Display a welcome message
    print("Welcome to the Weather Recommendation App!")

    # Ask for the user's weather-related query
    question = "Please enter your weather-related question. Remember to add your location:"
    print(question)

    # Allow the user to type in an answer
    request = input("Your question: ")

    # Get the location string
    location_string = get_location_string(request)

    # Get the weather by location
    weather_data = get_weather_by_location(location_string)

    # Analyze the weather based on the request
    analysis = analyze_weather(request, weather_data)

    # Display the weather information
    print(analysis)


if __name__ == "__main__":
    main()
