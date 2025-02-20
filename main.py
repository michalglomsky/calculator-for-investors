import csv
import os
from sqlalchemy import create_engine, String, Column, Float
from sqlalchemy.orm import sessionmaker, declarative_base


"""Functions for file and database management"""


def read_csv_as_dict(csv_path):
    """
    Opens a csv file and reads it into a dictionary

    :param csv_path:
    :return: table as a list of dictionaries
    """
    with open(csv_path, encoding='utf-8') as csv_file:
        return list(csv.DictReader(csv_file))


def add_dictionary(model, table_dictionary, session):
    """
     Maps each row of a table to an instance of the given model.

    :param model: The SQLAlchemy model class.
    :param table_dictionary: table represented as a list of dictionary.
    :param session: SQLAlchemy session.
    """
    for row in table_dictionary:
        for column_name, value in row.items():
            if value == '':  # Checking the exception
                row[column_name] = None
        session.add(model(**row))


Base = declarative_base()


class Companies(Base):
    __tablename__ = 'companies'
    ticker = Column("ticker", String(100), primary_key=True)
    name = Column("name", String(100))
    sector = Column("sector", String(100))


class Financial(Base):
    __tablename__ = 'financial'
    ticker = Column("ticker", String(100), primary_key=True)
    ebitda = Column("ebitda", Float)
    sales = Column("sales", Float)
    net_profit = Column("net_profit", Float)
    market_price = Column("market_price", Float)
    net_debt = Column("net_debt", Float)
    assets = Column("assets", Float)
    equity = Column("equity", Float)
    cash_equivalents = Column("cash_equivalents", Float)
    liabilities = Column("liabilities", Float)


# Dictionaries of attributes for our objects
financial_attributes = {column.name for column in Financial.__table__.columns}
companies_attributes = {column.name for column in Companies.__table__.columns}

"""Initializing the database and SQLAlchemy session"""

companies_path = "test/companies.csv"
financial_path = "test/financial.csv"
engine = ""
Session = ""
session = ""
if not os.path.exists("investor.db"):
    # If database hasn't been initialised, create it and add companies and financial tables
    engine = create_engine('sqlite:///investor.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    add_dictionary(Financial, read_csv_as_dict(financial_path), session)
    add_dictionary(Companies, read_csv_as_dict(companies_path), session)
else:
    # If database exists just maek a connection
    engine = create_engine('sqlite:///investor.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

"""Basic menu interface for investor's calculator (printed out in the console)"""

# Defining menus as a dictionary
MAIN_MENU = "MAIN MENU"
CRUD_MENU = "CRUD MENU"
TOPTEN_MENU = "TOP TEN MENU"
COMPANY_SEARCH_MENU = "COMPANY SEARCH MENU"

MENUS = {
    CRUD_MENU: {
        "0": "Back",
        "1": "Create a company",
        "2": "Read a company",
        "3": "Update a company",
        "4": "Delete a company",
        "5": "List all companies"
    },
    TOPTEN_MENU: {
        "0": "Back",
        "1": "List by ND/EBITDA",
        "2": "List by ROE",
        "3": "List by ROA"
    },
    MAIN_MENU: {
        "0": "Exit",
        "1": "CRUD operations",
        "2": "Show top ten companies by criteria"
    },
    COMPANY_SEARCH_MENU: {

    }
}

# Dictionary of console messages for queries about specific attributes
COMPANY_MESSAGES = {
    "ticker": "Enter ticker (in the format 'MOON'):\n> ",
    "name": "Enter company (in the format 'Moon Corp')\n> ",
    "sector": "Enter industries (in the format 'Technology'):\n> ",
    "ebitda": "Enter ebitda (in the format '987654321')\n> ",
    "sales": "Enter sales (in the format '987654321')\n> ",
    "net_profit": "Enter net profit (in the format '987654321')\n> ",
    "market_price": "Enter market price (in the format '987654321')\n> ",
    "net_debt": "Enter net debt (in the format '987654321')\n> ",
    "assets": "Enter assets (in the format '987654321')\n> ",
    "equity": "Enter equity (in the format '987654321')\n> ",
    "cash_equivalents": "Enter cash equivalents (in the format '987654321')\n> ",
    "liabilities": "Enter liabilities (in the format '987654321')\n> "
}


"""General menu functions"""


def print_menu(menu):
    """
    Displays a given menu to the console.
    """
    print(menu)
    for k, v in MENUS[menu].items():
        print(f"{k} {v}")


def get_option(menu):
    """
    Displays a given menu and asks for a valid menu option until given one
    """
    print_menu(menu)
    while (option := input("Enter an option: ")) not in MENUS[menu]:
        print("Invalid option!")
        print_menu(menu)
    return option


def sub_menu(menu):
    """
    Opens CRUDE or TOP TEN menu and asks for a valid menu option until given.
    """
    option = get_option(menu)
    if option != "0":
        if menu == CRUD_MENU:
            crud_menu(option)
        elif menu == TOPTEN_MENU:
            topten_menu(option)
        main_menu()
    else:
        main_menu()


def main_menu():
    """
    Opens MAIN MENU which opens either CRUDE or TOP TEN menus
    """
    option = get_option(MAIN_MENU)
    if option == "0":
        print("Have a nice day!")
    elif option == "1":
        sub_menu(CRUD_MENU)
    elif option == "2":
        sub_menu(TOPTEN_MENU)


"""CRUD MENU functions"""


def crud_menu(option):
    """
    Function navigating through crud menu functions.

    :param option: function to be opened
    """
    if option == "1":
        company_create()
    elif option == "2":
        company_read()
    elif option == "3":
        company_update()
    elif option == "4":
        company_delete()
    elif option == "5":
        company_list_all()


def company_create():
    """
    Create a company record in the database (both tables)
    """
    company = Companies()
    financial = Financial()

    ticker = input("Enter ticker (in the format 'MOON'):\n> ")
    company.ticker = ticker
    financial.ticker = ticker
    company.name = input("Enter company (in the format 'Moon Corp'):\n> ")
    company.sector = input("Enter industries (in the format 'Technology'):\n> ")
    financial.ebitda = float(input("Enter ebitda (in the format '987654321'):\n> "))
    financial.sales = float(input("Enter sales (in the format '987654321'):\n> "))
    financial.net_profit = float(input("Enter net profit (in the format '987654321'):\n> "))
    financial.market_price = float(input("Enter market price (in the format '987654321'):\n> "))
    financial.net_debt = float(input("Enter net debt (in the format '987654321'):\n> "))
    financial.assets = float(input("Enter assets (in the format '987654321'):\n> "))
    financial.equity = float(input("Enter equity (in the format '987654321'):\n> "))
    financial.cash_equivalents = float(input("Enter cash equivalents (in the format '987654321'):\n> "))
    financial.liabilities = float(input("Enter liabilities (in the format '987654321'):\n> "))

    session.add(financial)
    session.add(company)
    session.commit()
    # Success message
    print("Company created successfully!")


def company_search_menu(name):
    """
    Based on the name given by the user, look for company names in the database that include that name.
    Returns a menu dictionary of these companies.

    :param: string name of a dictionary
    :return: menu dictionary
    """
    query = session.query(Companies).all()
    counter = 0
    # Clearing the COMPANY_SEARCH_MENU
    menu = MENUS[COMPANY_SEARCH_MENU] = {}
    for company in query:
        if name.casefold() in company.name.casefold():
            menu[str(counter)] = company.name
            counter += 1
    return menu


def company_read_calculations(financial):
    """
    Calculations for the company_read() function.
    P/E = Market price / Net profit
    P/S = Market price / Sales
    P/B = Market price / Assets
    ND/EBITDA = Net debt / EBITDA
    ROE = Net profit / Equity
    ROA = Net profit / Assets
    L/A = Liabilities / Assets

    :param financial: Financial object
    :return: None
    """
    try:
        print("P/E =", round(financial.market_price / financial.net_profit, 2))
    except TypeError:
        print("P/E =", None)
    try:
        print("P/S =", round(financial.market_price / financial.sales, 2))
    except TypeError:
        print("P/S =", None)
    try:
        print("P/B =", round(financial.market_price / financial.assets, 2))
    except TypeError:
        print("P/B =", None)
    try:
        print("ND/EBITDA =", round(financial.net_debt / financial.ebitda, 2))
    except TypeError:
        print("ND/EBITDA =", None)
    try:
        print("ROE =", round(financial.net_profit / financial.equity, 2))
    except TypeError:
        print("ROE =", None)
    try:
        print("ROA =", round(financial.net_profit / financial.assets, 2))
    except TypeError:
        print("ROA =", None)
    try:
        print("L/A =", round(financial.liabilities / financial.assets, 2))
    except TypeError:
        print("L/A =", None)


# Better to define a class for this functionality
def company_name_to_ticker():
    """
    Based on a name from input looks for companies that fit it, lets user choose from a menu of these companies
    and then returns ticker and name of a chosen company

    :return: Tuple of (ticker, company_name)
    """
    name = input("Enter company name:")
    menu = company_search_menu(name)
    if menu != {}:
        for k, v in menu.items():
            print(f"{k} {v}")
        option = input("Enter company number:")
        company_name = menu.get(option)
        # Find ticker in Companies based on name, to find proper company in Financial
        ticker = session.query(Companies.ticker).filter(Companies.name == company_name).first()[0]
        return ticker, company_name
    else:
        return None


def company_read():
    """
    Uses company_name_to_ticker to find a company name, find fitting names in the database
    and then uses company_read_calculations() for calculations and printing the statistics.
    """
    result = company_name_to_ticker()
    if result is not None:
        ticker, company_name = result
        print(ticker, company_name)
        query = session.query(Financial).filter(Financial.ticker == ticker)
        for financial in query:
            company_read_calculations(financial)
    else:
        print("Company not found!")

def company_update():
    """
    Updates companies financial information.
    """
    ticker = company_name_to_ticker()[0]
    if ticker is not None:
        query = session.query(Financial).filter(Financial.ticker == ticker)
        # Updating the database

        # Create a dictionary with user inputs for each key
        update_values = {
            key: input(prompt)
            for key, prompt in COMPANY_MESSAGES.items()
            if key != "ticker" and key in financial_attributes
        }
        # Then update your query with the collected values
        query.update(update_values)
        print("Company updated successfully!")
        session.commit()
    else:
        print("Company not found!")


def company_delete():
    """
    Deletes a company from a database.
    """
    ticker = company_name_to_ticker()[0]
    if ticker is not None:
        # Deleting company from both tables
        session.query(Financial).filter(Financial.ticker == ticker).delete()
        session.query(Companies).filter(Companies.ticker == ticker).delete()
        session.commit()
        print("Company deleted successfully!")

    else:
        print("Company not found!")


def company_list_all():
    """
    Lists all companies currently in the Companies table
    """
    print("COMPANY LIST")
    companies_list = [[company.ticker, company.name, company.sector] for company in session.query(Companies).all()]
    for company in sorted(companies_list, key=lambda x: x[0]):
        print(company[0], company[1], company[2])


"""Top Ten Menu functions"""


def topten_menu(option):
    """
    Top Ten Menu function, yet to be implemented.
    """
    print("Not implemented!")


"""Main function running the program"""


def main():
    # Initializing the program by displaying MAIN MENU
    print("Welcome to the Investor Program!")
    main_menu()
    session.commit()
    session.close()

if __name__ == '__main__':
    main()