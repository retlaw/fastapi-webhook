from sqlalchemy import Column, String, Integer
from database import Base

class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    post = Column(String, index=True)