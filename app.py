from flask import Flask, render_template, request, jsonify
# from database import get_history, init_db, save_weather
from services.weather_service import get_weather
from models import db, Weather

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'  # configure the database URI for SQLAlchemy
db.init_app(app)  # initialize SQLAlchemy with the Flask app

# init_db()  # ensure the database tables exist before the app starts
with app.app_context():
    if db.engine.has_table('weather'):
        db.drop_all()  # drop existing tables to reset schema
    db.create_all()  # create the database tables based on the defined models

@app.route('/', methods=['GET', 'POST'])  # normal page open (GET), form submit (POST)
def home():
    city = ""
    error = None
    data = None

    if request.method == 'POST':  # when form is submitted
        city = request.form.get("city", "").strip()  # get city name from form input

        if not city:
            error = "Please enter a city name."
        else:
            data = get_weather(city)  # call the function to get weather data for the city
            if data is None:
                error = "City not found or error fetching data."
            else:
                # save_weather(
                #     city,
                #     data['main']['temp'],
                #     data['main']['humidity'],
                #     data['weather'][0]['description']
                # )
                new_weather = Weather(
                    city = city,
                    temperature = data['main']['temp'],
                    humidity = data['main']['humidity'],   
                    description = data['weather'][0]['description']
                )
                db.session.add(new_weather)
                db.session.commit()
    return render_template('index.html', data=data, city=city, error=error)  # to display HTML page with data, city and error

@app.route('/api/weather', methods=['POST'])  # backend API endpoint
def api_weather():
    json_data = request.get_json(silent=True) or {}
    city = (json_data.get("city") or "").strip()
    if not city:
        return jsonify({
            "success": False,
            "error": "City not provided"
        }), 400
    
    data = get_weather(city)
    if data:
        return jsonify({
            "success": True,
            "data": data
        }), 200
    return jsonify({
        "success": False,
        "error": "City not found"
    }), 404

@app.route('/history')  # to display the weather history page
def history():
#     # record = get_history()  # this function will retrieve the weather history from the database
#     history_data = [
#       # {
#       #   "city": record[1],
#       #   "data": record[2]
#       # }
#     ] 
    records = Weather.query.all()  # query all weather records from the database
    history_data = []
    for record in records:
        history_data.append({
            "city": record.city,
            "temperature": record.temperature,
            "humidity": record.humidity,
            "description": record.description       
        })
    return jsonify(history_data), 200  # return the history data as JSON response with status code 200

@app.route("/history/<city>")  # to display the weather history for a specific city
def city_history(city):
    records = (
        Weather.query
        .filter_by(city=city)
        .order_by(Weather.timestamp.desc())
        .limit(5)
        .all()
    )
    city_history_data = [
        {
            "city": record.city,
            "temperature": record.temperature,
            "humidity": record.humidity,
            "description": record.description,
            "timestamp": record.timestamp.isoformat()
        }
        for record in records
    ]
    return jsonify(city_history_data), 200

if __name__ == '__main__':
    app.run(debug=True)  # to run the Flask app in debug mode