import httpx
from dotenv import load_dotenv
import os 
from app.models.external_data import StockData

load_dotenv()

class StocksClient:
    URL = "https://finnhub.io/api/v1/quote"
    API_KEY = os.getenv("STOCK_API_KEY")

    async def get_stock_data(self, symbol: str) -> StockData:
        params = {
            "symbol": symbol,
            "token": self.API_KEY
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(self.URL, params=params)
            response.raise_for_status()
            data = response.json()
            return StockData(symbol=symbol,
                             current_price=data["c"],
                             change_percent=data["dp"])