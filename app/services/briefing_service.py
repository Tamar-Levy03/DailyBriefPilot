from app.clients.weather_client import WeatherClient

class BriefingService:

    def __init__(self):
        self.weather_client = WeatherClient()
        

    async def generate_briefing(self) -> str:
        weather = await self.weather_client.get_weather()
        location = weather["location"]["name"]
        temperature = weather["current"]["temp_c"]
        condition = weather["current"]["condition"]["text"]
        briefing = f"the weather in {location} is currently {condition} with a temperature of {temperature} Celsius"
        return briefing