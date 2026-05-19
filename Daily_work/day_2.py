import os
from dotenv import load_dotenv

# Get path to the .env file in the project root (parent directory of Daily_work)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
load_dotenv(os.path.join(project_root, ".env"))

# api key from the OpenWeatherMap
api_key = os.getenv("OPENWEATHER_API_KEY")

#create a function to input the city and get the ouput as temperature

import requests

def get_temperature(city):
    if not api_key:
        print("Error: OPENWEATHER_API_KEY is not defined in your environment or .env file.")
        return None

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['main']['temp']
    elif response.status_code == 401:
        data = response.json()
        print(f"Error 401: {data.get('message')}")
        print("Note: If you just created this API key, it typically takes 10 to 60 minutes (and up to 2 hours) to activate.")
        return None
    else:
        data = response.json()
        print(f"Error {response.status_code}: {data.get('message', 'Failed to retrieve data')}")
        return None

# Test the function
temp = get_temperature("chennai")
if temp is not None:
    print(f"The temperature in Chennai is {temp} Kelvin")