import os
import httpx
from dotenv import load_dotenv
import app.models.external_data as external_data

load_dotenv()

class OpenRouterClient:
    URL = "https://openrouter.ai/api/v1/chat/completions"
    API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

    async def generate_briefing(self, weather:external_data.WeatherData, stocks:external_data.StockData, news:list[external_data.NewsArticle]) -> str:
        headers = {"Authorization": f"Bearer {self.API_KEY}",
                     "Content-Type": "application/json"}
        news_titles = "\n".join([f"- {article.title}" for article in news])
        model = os.getenv("OPENROUTER_MODEL")
        prompt = f"""Write a friendly morning daily briefing in Hebrew for Tamar.
        Use only the data below. Do not invent facts.
        Weather:
        City: {weather.city}
        Condition: {weather.condition}
        Temperature: {weather.temperature} Celsius
        
        Stock:
        Symbol: {stocks.symbol}
        Current price: {stocks.current_price}
        Change percent: {stocks.change_percent}
        
        News headlines:
        {news_titles}
        
        The message should:
        - Start with a warm good morning to Tamar
        - Mention the weather
        - Mention the stock movement
        - Mention the main news headlines
        - End with a short positive sentence
        - Be concise and natural
        """

        body = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You write concise, friendly daily briefings in Hebrew."},
                {"role": "user", "content": prompt}
            ],
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.URL, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]