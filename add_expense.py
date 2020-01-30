from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from creating_table import Expenses

Base = declarative_base()


def adding_expenses(expense: Expenses):
    engine = create_engine("mysql+pymysql://MY_CHANGES")
    engine.execute("USE dailyExpenses")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    session.add(expense)

    session.commit()

    session.close()
