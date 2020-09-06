from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class Alert(BaseModel):
    name: str
    description: Optional[str] = None
    dateTime: int = None
    tax: Optional[float] = None

class City(BaseModel):
    name: str
    timezone: str 
 
class Any(BaseModel):
    any: dict

db = []

@app.get("/")
def read_root():
    with open('access.txt', 'a') as f:
        f.write('i have been accessed\n')
    return {"Hello": "FastApi"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get('/cities')
def get_cities():
    return db

# @app.get('/cities/{city_id}')

@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1] 

@app.post('/any')
def create_any(mydict: dict):
    return mydict

# @app.delete('/cities')

@app.put("/items/{item_id}")
def udpate_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/meraki/alerts/")
def meraki(q: Optional[str]):
    return {q: q}