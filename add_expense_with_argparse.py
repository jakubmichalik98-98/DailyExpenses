from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import argparse
from datetime import datetime
from creating_table import Expenses

Base = declarative_base()
parser = argparse.ArgumentParser(description="Add expense with argparse module")
parser.add_argument("-i", "--id", type=int, metavar="", required=True, help="Id in database")
parser.add_argument("-p", "--product", type=str, metavar="", required=True, help="name of adding product")
parser.add_argument("-pr", "--price", type=float, metavar="", required=True, help="price of a product")
parser.add_argument("-d", "--date_added", default=datetime.now(), help="date of adding")
parser.add_argument("-c", "--category", type=str, metavar="", required=True, help="category of a product")
args = parser.parse_args()


def adding_expenses(id, product, price, date_added, category):
    engine = create_engine("mysql+pymysql://MY_CHANGES")
    engine.execute("USE dailyExpenses")
    Base.metadata.create_all(engine)

    expense = Expenses(id=id, product=product, price=price, date_added=date_added, category=category)

    print(expense)

    Session = sessionmaker(bind=engine)

    session = Session()

    session.add(expense)

    session.commit()

    session.close()


if __name__ == '__main__':
    adding_expenses(args.id, args.product, args.price, args.date_added, args.category)