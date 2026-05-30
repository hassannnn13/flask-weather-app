# Flask Weather App

A simple weather application built with Flask that allows users to search for weather information of any city using the OpenWeatherMap API.

## Features

- Search weather by city name
- Displays:
  - Temperature
  - Feels Like Temperature
  - Humidity
  - Wind Speed
  - Weather Description
- Weather condition emojis
- Error handling for invalid cities
- Weather search history stored in SQLite database
- Built using Flask and SQLAlchemy ORM

## Technologies 

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML
- CSS
- OpenWeatherMap API

## Project Structure

WeatherApp/
│
├── app.py
├── models.py
├── services/
│ └── weather_service.py
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css
│
├── requirements.txt
└── README.md

## Installation

1. Clone the repository
```bash
git clone <repository-url>

2. Navigate to the project
cd weather-app

3. Install dependencies
pip install -r requirements.txt

4. Add your OpenWeatherMap API key
api_key = "YOUR_API_KEY"

5. Run the application
python app.py

## Author
Hassan Idrees
