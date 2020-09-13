from fastapi import FastAPI, Request, Depends
from pydantic import BaseModel

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

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
 
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close_all()
# db = []

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"Hello": "FastApi", "database": db.query(Posts).all()}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q} 

# @app.get('/cities')
# def get_cities():
#     return db

# @app.get('/cities/{city_id}')

# @app.post('/cities')
# def create_city(city: City):
#     db.append(city.dict())
#     return db[-1] 

# @app.delete('/cities')

@app.put("/items/{item_id}")
def udpate_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/meraki/alerts/")
def meraki(q: Optional[str]):
    return {q: q}