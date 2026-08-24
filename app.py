from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Get the OpenWeather API key from the environment
API_KEY = os.getenv("WEATHER_API_KEY")


# Home route to confirm that the API is running
@app.route("/")
def home():
    return jsonify({
        "message": "Weather API is running"
    })


# Weather route: receives a city and returns its current weather data
@app.route("/weather")
def get_weather():

    # Get the city name from the URL query parameter
    city = request.args.get("city")

    # Return an error if no city was provided
    if not city:
        return jsonify({
            "error": "City is required"
        }), 400

    # OpenWeather API endpoint
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Parameters sent to the OpenWeather API
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        # Send the request to OpenWeather with a 5-second timeout
        response = requests.get(
            url,
            params=params,
            timeout=5
        )
    except requests.RequestException:
        # Handle connection errors or unavailable weather service
        return jsonify({
            "error": "Weather service is currently unavailable"
        }), 503

    # Convert the API response from JSON into a Python dictionary
    data = response.json()

    # Return the error provided by OpenWeather if the request failed
    if response.status_code != 200:
        return jsonify({
            "error": data.get("message", "Unable to get weather data")
        }), response.status_code

    # Return only the weather information needed by our API
    return jsonify({
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    })


# Start the Flask development server when this file is run directly
if __name__ == "__main__":
    app.run(debug=True)