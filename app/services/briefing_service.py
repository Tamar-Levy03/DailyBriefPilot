from app.clients.weather_client import WeatherClient
from app.clients.stocks_client import StocksClient
from app.clients.news_client import NewsClient
import asyncio
from app.clients.openrouter_client import OpenRouterClient

class BriefingService:

    def __init__(self):
        self.weather_client = WeatherClient()
        self.stocks_client = StocksClient()
        self.news_client = NewsClient()
        self.openrouter_client = OpenRouterClient()

    async def generate_briefing(self) -> str:
        weather, stocks, news = await asyncio.gather(
            self.weather_client.get_weather(),
            self.stocks_client.get_stock_data("AAPL"),
            self.news_client.get_news()
        )
        briefing_message = await self.openrouter_client.generate_briefing(weather=weather, stocks=stocks, news=news)
        return briefing_message
    