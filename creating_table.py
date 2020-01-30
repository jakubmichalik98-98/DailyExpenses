from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Integer, String, Float, DateTime

Base = declarative_base()


class Expenses(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, name="Id")
    product = Column(String(30), name="Product")
    price = Column(Float, name="Price")
    date_added = Column(DateTime, name="DateAdded")
    category = Column(String(30), name="Category")

    def __repr__(self):
        return f"Expense: {self.id}, product {self.product}, price: {self.price}, date added: {self.date_added}"


if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://MY_CHANGES", echo=True)
    engine.execute("USE dailyExpenses")
    Base.metadata.create_all(engine)


