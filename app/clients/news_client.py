import httpx
from dotenv import load_dotenv
import os
from app.models.external_data import NewsArticle

load_dotenv()

class NewsClient:
    URL = "https://gnews.io/api/v4/top-headlines"
    API_KEY = os.getenv("GNEWS_API_KEY")

    async def get_news(self) -> list[NewsArticle]:
        params = {
            "apikey": self.API_KEY,
            "country": "il", #israel for testing, can be changed to any country
            "lang": "he", #hebrew for testing, can be changed to any language
            "category": "general", #general news for testing, can be changed to any category
            "max": 3
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(self.URL, params=params)
            response.raise_for_status()
            data = response.json()
            news_items = []
            for article in data["articles"]:
                if article.get("title"):
                    news_article = NewsArticle(
                        title=article["title"],
                        description=article.get("description"),
                        source=article.get("source", {}).get("name"),
                        url=article.get("url")
                    )
                    news_items.append(news_article)
            return news_items