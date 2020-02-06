from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from creating_table import Expenses
import argparse

Base = declarative_base()
parser = argparse.ArgumentParser(description="Display expense with argparse module")
parser.add_argument("-f", "--from_date", required=True, metavar="", help="Beginning of the time period")
parser.add_argument("-t", "--to_date", required=True, metavar="", help="End of the time period")
args = parser.parse_args()


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


if __name__ == '__main__':
    display_expense(args.from_date, args.to_date)
