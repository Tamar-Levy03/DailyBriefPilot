import httpx

class WeatherClient:
    URL ="https://api.open-meteo.com/v1/forecast"
    
    async def get_weather(self,) -> dict:
        params = {
            "latitude": 32.573905,
            "longitude": 34.951977,    #Zichron yaakov coordinates for testing
            "current": "temperature_2m"
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(self.URL, params=params)
            response.raise_for_status()
            return response.json()