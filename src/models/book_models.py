from sqlalchemy import  Column, Integer, String
from src.database.db import Base

class Book(Base):
    __tablename__ ="book"

    id = Column(Integer, primary_key=True, autoincrement=False,index=True)
    title = Column(String)
    description = Column(String)