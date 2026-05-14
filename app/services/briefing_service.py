from app.clients.weather_client import WeatherClient
from app.clients.stocks_client import StocksClient

class BriefingService:

    def __init__(self):
        self.weather_client = WeatherClient()
        self.stocks_client = StocksClient()

    async def generate_briefing(self) -> str:
        #weather briefing
        weather = await self.weather_client.get_weather()
        location = weather["location"]["name"]
        temperature = weather["current"]["temp_c"]
        condition = weather["current"]["condition"]["text"]
        briefing = f"the weather in {location} is currently {condition} with a temperature of {temperature} Celsius\\n"
        #stocks briefing
        stocks = await self.stocks_client.get_stock_data("AAPL")
        stock_price = stocks["c"]
        change_percent = stocks["dp"]
        briefing += f"The current price of AAPL is ${stock_price} with a change of {change_percent}%."
        return briefing