from app.clients.weather_client import WeatherClient
from app.clients.stocks_client import StocksClient
from app.clients.news_client import NewsClient

class BriefingService:

    def __init__(self):
        self.weather_client = WeatherClient()
        self.stocks_client = StocksClient()
        self.news_client = NewsClient()

    async def generate_briefing(self) -> str:
        #weather briefing
        weather = await self.weather_client.get_weather()
        location = weather["location"]["name"]
        temperature = weather["current"]["temp_c"]
        condition = weather["current"]["condition"]["text"]
        briefing = f"the weather in {location} is currently {condition} with a temperature of {temperature} Celsius\n"
        #stocks briefing
        stocks = await self.stocks_client.get_stock_data("AAPL")
        stock_price = stocks["c"]
        change_percent = stocks["dp"]
        briefing += f"The current price of AAPL is ${stock_price} with a change of {change_percent}%."
        #news briefing
        news = await self.news_client.get_news()
        articles = news["articles"]
        headlines = [article["title"] for article in articles]
        briefing += "\nToday's top news headlines are:\n" + "\n".join(headlines)

        return briefing
    
    