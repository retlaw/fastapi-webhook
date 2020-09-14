from typing import Optional
from fastapi import FastAPI, Request, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()
app = FastAPI()


class User(Base):
    __tablename__ = "user"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, unique=True)


class Alert(Base):
    __tablename__ = "alert"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    alert = Column('alert', String)


engine = create_engine(
    # 'postgresql://puser:ppassword@localhost:5432',
    # echo=True
    'sqlite:///users.db',
    echo=True
    # 'postgres://dqssehkxoescfl:0078d16323a2b20ed3c2f4fe5c4ded01517bb7a76ad730920591c0ae106b2c58@ec2-35-174-88-65.compute-1.amazonaws.com:5432/dd07jb9ubigs6g',
    # echo=False
)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


# user = User()
# user.username = "Charntil"




class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

# class Alert(BaseModel):
#     name: str
#     description: Optional[str] = None
#     dateTime: int = None
#     tax: Optional[float] = None

class City(BaseModel):
    name: str
    timezone: str 


class MyUser(BaseModel):
    username: str

# db = []


@app.get("/")
def read_root():
    return {"Hello": "FastApi"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q} 


@app.post("/users")
def add_user(this_user: MyUser):
    session = Session()
    user = User()
    user.username = this_user.username
    session.add(user)
    session.commit()
    users = session.query(User).all()
    for user in users:
        print(user.username, user.id)
    session.close()
    return users

# @app.get('/cities')
# def get_cities():
#     return db


@app.get("/all-alerts")
def get_alerts():
    session = Session()
    alerts = session.query(Alert).all()
    # for user in users:
    #     print(user.username, user.id)
    session.close()
    return alerts


# @app.get('/cities/{city_id}')

# @app.post('/cities')
# def create_city(city: City):
#     db.append(city.dict())
#     return db[-1] 

# @app.delete('/cities')


@app.put("/items/{item_id}")
def udpate_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/sdwan/alerts")
def meraki(post: dict):
    session = Session()
    alert = Alert()
    alert.alert = str(post)
    session.add(alert)
    session.commit()
    # users = session.query(User).all()
    # for user in users:
    #     print(user.username, user.id)
    session.close()
    return {"alert": post}
