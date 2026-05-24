import requests
# from database import init_db # Import the init_db function from the database module 

# init_db()  # Call the init_db function to ensure the database tables are created before any operations are performed

def get_weather(city): 
    api_key = "9ed903eb685e874e77e2d8c9ae13e190"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url) # get url response from the API

    if response.status_code == 200:
        return response.json()
    else:
        return None