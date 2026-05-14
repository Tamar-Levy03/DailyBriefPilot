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
        location = weather["location"]["name"]
        temperature = weather["current"]["temp_c"]
        condition = weather["current"]["condition"]["text"]
        weather_briefing = f"the weather in {location} is currently {condition} with a temperature of {temperature} Celsius."
        #stocks briefing
        stock_price = stocks["c"]
        change_percent = stocks["dp"]
        stocks_briefing = f"The current price of AAPL is ${stock_price} with a change of {change_percent}%."
        #news briefing
        articles = news["articles"]
        headlines = [article["title"] for article in articles]
        news_briefing = "\nToday's top news headlines are:\n" + "\n".join(headlines)
        briefing = "\n".join([weather_briefing, stocks_briefing, news_briefing])
        return briefing
    
    