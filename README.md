# Weather API

A simple RESTful Weather API built with **Python** and **Flask**. It retrieves current weather information from the **OpenWeather API** and returns the data in JSON format.

## Features

* Get weather information for any city.
* Returns temperature in Celsius.
* Returns "feels like" temperature.
* Returns humidity.
* Returns current weather conditions.
* Returns wind speed.
* Handles missing city parameters.
* Handles unavailable weather services.
* Keeps the OpenWeather API key secure using environment variables.

## Technologies Used

* Python
* Flask
* Requests
* python-dotenv
* OpenWeather API

## Project Structure

```text
weather-api/
│
├── app.py
├── requirements.txt
├── .gitignore
└── .env
```

## Installation

Clone the repository:

```bash
git clone https://github.com/SammyDev19/weather-api.git
cd weather-api
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project directory:

```env
WEATHER_API_KEY=your_openweather_api_key
```

Replace `your_openweather_api_key` with your actual OpenWeather API key.

**Do not commit the `.env` file to GitHub.** It is included in `.gitignore` to keep the API key private.

## Running the API

Start the Flask development server:

```bash
python app.py
```

The API will run locally at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### Home

```text
GET /
```

Returns a message confirming that the API is running.

Example response:

```json
{
    "message": "Weather API is running"
}
```

### Get Weather

```text
GET /weather?city=London
```

Returns the current weather information for the specified city.

Example response:

```json
{
    "city": "London",
    "country": "GB",
    "temperature": 18.5,
    "feels_like": 17.9,
    "humidity": 72,
    "condition": "overcast clouds",
    "wind_speed": 3.1
}
```

### Error Responses

If no city is provided:

```text
GET /weather
```

The API returns:

```json
{
    "error": "City is required"
}
```

with HTTP status `400`.

If the external weather service is unavailable, the API returns HTTP status `503`.

## Purpose

This project was built as a practice project for learning **Flask, REST APIs, HTTP requests, environment variables, and working with external APIs**.
