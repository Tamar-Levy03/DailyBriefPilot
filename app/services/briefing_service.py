from app.clients.weather_client import WeatherClient
from app.clients.stocks_client import StocksClient
from app.clients.news_client import NewsClient
import asyncio

class BriefingService:

    def __init__(self):
        self.weather_client = WeatherClient()
        self.stocks_client = StocksClient()
        self.news_client = NewsClient()

    async def generate_briefing(self) -> str:
        weather, stocks, news = await asyncio.gather(
            self.weather_client.get_weather(),
            self.stocks_client.get_stock_data("AAPL"),
            self.news_client.get_news()
        )
        #weather briefing
        weather_briefing = f"the weather in {weather.city} is currently {weather.condition} with a temperature of {weather.temperature} Celsius."
        #stocks briefing
        stocks_briefing = f"The current price of AAPL is ${stocks.current_price} with a change of {stocks.change_percent}%."
        #news briefing
        news_briefing = "\nToday's top news headlines are:\n" + "\n".join([article.title for article in news])
        briefing = "\n".join([weather_briefing, stocks_briefing, news_briefing])
        return briefing
    
    