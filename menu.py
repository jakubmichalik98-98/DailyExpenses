from creating_table import Expenses
from add_expense import adding_expenses
from datetime import datetime
from display_expense import display_expense

CATEGORIES = {"food", "drinks", "entertainment", "fuel", "sport", "electronics"}


class ChosenError(Exception):
    """raises when user don't choose [y] or [n]"""


def main():
    print("Hello in your daily expenses application!")
    choose = input("Do you wanna add or display expense? If add click [y] if display click [n] ")

    if choose == "y":
        product = input("Enter the name of product: ")
        price = float(input("Enter the price of a product: "))
        date_added = datetime.now()
        print(f"Available categories: {CATEGORIES}")
        category = input("Enter category of a product: ")
        if category in CATEGORIES:
            pass
        else:
            category = None

        added_expense = Expenses(product=product, price=price, date_added=date_added, category=category)
        adding_expenses(added_expense)

    elif choose == "n":
        from_date = datetime(2020, 1, 1)
        to_date = datetime(2020, 10, 10)
        display_expense(from_date, to_date)

    else:
        raise ChosenError


if __name__ == '__main__':
    main()
