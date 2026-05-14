import httpx
from dotenv import load_dotenv
import os 

load_dotenv()

class StocksClient:
    URL = "https://finnhub.io/api/v1/quote"
    API_KEY = os.getenv("STOCK_API_KEY")

    async def get_stock_data(self, symbol: str) -> dict:
        params = {
            "symbol": symbol,
            "token": self.API_KEY
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(self.URL, params=params)
            response.raise_for_status()
            return response.json()