from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class MyTable(Base):
    __tablename__ = "my_table"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100))


try:
    engine = create_engine("postgresql://shipay:shipay@localhost:5432/shipayDB")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    teste = MyTable()
    session.commit()
    session.close()
    print("Table created successfully.")
except Exception as e:
    print("Error occurred:", str(e))
