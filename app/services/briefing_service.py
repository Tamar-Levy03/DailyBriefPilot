from app.clients.weather_client import WeatherClient

class BriefingService:

    def __init__(self):
        self.weather_client = WeatherClient()
        

    async def generate_briefing(self) -> str:
        weather = await self.weather_client.get_weather()
        temperature = weather["current"]["temperature_2m"]
        briefing = f"the temperature in zichron yaakov is currently {temperature} Celsius"
        return briefing