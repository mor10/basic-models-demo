import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Function to get location data from OpenWeatherMap Geocoding API
def get_location_data(location, limit=1):
    owm_api_key = os.getenv('OWM_API_KEY')  # Get API key from environment variable
    if not owm_api_key:
        return {"error": "API key not found."}
    
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    
    params = {
        'q': location,
        'limit': limit,
        'appid': owm_api_key
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        data = response.json()
        if data:
            # Extract required information
            extracted_data = []
            for item in data:
                extracted_info = {
                    'name': item.get('name'),
                    'lat': item.get('lat'),
                    'lon': item.get('lon'),
                    'country': item.get('country')
                }
                extracted_data.append(extracted_info)
            return extracted_data
        else:
            return {"error": "No data found for the specified location."}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    

# Function to get weather data from OpenWeatherMap API
def get_weather_data(location_data):
    owm_api_key = os.getenv('OWM_API_KEY')  # Get API key from environment variable
    if not owm_api_key:
        return {"error": "API key not found."}
    
    if not location_data or 'lat' not in location_data or 'lon' not in location_data:
        return {"error": "Invalid location data."}

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'lat': location_data['lat'],
        'lon': location_data['lon'],
        'appid': owm_api_key
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Function to get weather data based on location
def get_weather_by_location(location):
    location_data = get_location_data(location)
    
    if isinstance(location_data, dict) and "error" in location_data:
        return location_data
    
    if not location_data:
        return {"error": "Failed to get location data."}
    
    weather_data = get_weather_data(location_data[0])
    
    return weather_data