import httpx
from dotenv import load_dotenv
import os
from app.models.external_data import WeatherData

load_dotenv()

class WeatherClient:
    URL ="http://api.weatherapi.com/v1/current.json"
    API_KEY = os.getenv("WEATHER_API_KEY")

    async def get_weather(self,) -> WeatherData:
        params = {
            "key": self.API_KEY,
            "q": "Zikhron Ya'akov, Israel", #Zichron yaakov for testing, can be changed to any location
            "aqi": "no"
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(self.URL, params=params)
            response.raise_for_status()
            data = response.json()
            return WeatherData(city=data["location"]["name"],
                               temperature=data["current"]["temp_c"],
                               condition=data["current"]["condition"]["text"],)