from pydantic import BaseModel

class WeatherData(BaseModel):
    city: str
    temperature: float
    condition: str

class StockData(BaseModel):
    symbol: str
    current_price: float
    change_percent: float

class NewsArticle(BaseModel):
    title: str
    description: str | None = None
    sorce: str | None = None
    url: str | None = None