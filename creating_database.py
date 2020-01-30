from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://MY_CHANGES", echo=True)
    engine.execute("CREATE DATABASE dailyExpenses")
    engine.execute("USE dailyExpenses")