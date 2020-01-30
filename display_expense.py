from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from creating_table import Expenses

Base = declarative_base()


def display_expense(from_date, to_date):
    engine = create_engine("mysql+pymysql://MY_CHANGES")
    engine.execute("USE dailyExpenses")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    for expense in session.query(Expenses).filter(Expenses.date_added > from_date).filter(
            Expenses.date_added < to_date):
        print(expense)

    session.close()
