from database.config import Base
from sqlalchemy import Column, Integer, String


class MyTable(Base):
    __tablename__ = "my_table"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100))
