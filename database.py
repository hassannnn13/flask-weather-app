# from datetime import datetime
# import sqlalchemy

# # class Weather(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     city = db.Column(db.String(100), nullable=False)
#     temperature = db.Column(db.Float, nullable=False)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# def init_db():  # this function will create the database tables if they don't exist
#     conn = sqlite3.connect('weather.db')
#     cursor = conn.cursor() # executes SQL commands
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS weather_cache (
#             city TEXT PRIMARY KEY,
#             data TEXT
#         )
#     ''')
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS weather_history (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             city TEXT,
#             data TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# def save_weather(city, temperature, humidity, description):  # this function will save the weather data for a city into the database
#     conn = sqlite3.connect('weather.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT INTO weather_history (city, data)
#         VALUES (?, ?)
#     ''', (city, f"{temperature},{humidity},{description}"))
#     conn.commit()
#     conn.close()

# def get_history():  # this function will retrieve the weather history from the database
#     conn = sqlite3.connect('weather.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM weather_history')
#     history = cursor.fetchall()
#     conn.close()
#     return history
