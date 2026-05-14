import httpx
from dotenv import load_dotenv
import os

load_dotenv()

class WeatherClient:
    URL ="http://api.weatherapi.com/v1/current.json"
    API_KEY = os.getenv("WEATHER_API_KEY")

    async def get_weather(self,) -> dict:
        params = {
            "key": self.API_KEY,
            "q": "Zikhron Ya'akov, Israel", #Zichron yaakov for testing, can be changed to any location
            "aqi": "no"
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(self.URL, params=params)
            response.raise_for_status()
            return response.json()