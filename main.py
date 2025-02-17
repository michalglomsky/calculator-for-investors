import csv
import os
from sqlalchemy import create_engine, String, Column, Float
from sqlalchemy.orm import sessionmaker, declarative_base

def check_db(db_path):
    """
    Checks if the database exists, if yes resets it by deleting it

    :param db_path: database path
    """
    if os.path.exists(db_path):
        os.remove(db_path)

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
        for column_name, value  in row.items():
            if value == '': # Checking the exception
                row[column_name] = None
        session.add(model(**row))

Base = declarative_base()

class Companies(Base):
    __tablename__ = 'companies'
    ticker = Column(String(100), primary_key=True)
    name = Column(String(100))
    sector = Column(String(100))

class Financial(Base):
    __tablename__ = 'financial'
    ticker = Column(String(100), primary_key=True)
    ebitda = Column(Float)
    sales = Column(Float)
    net_profit = Column(Float)
    market_price = Column(Float)
    net_debt = Column(Float)
    assets = Column(Float)
    equity = Column(Float)
    cash_equivalents = Column(Float)
    liabilities = Column(Float)

def main():

    # Initialize the db and session
    check_db("investor.db")
    engine = create_engine('sqlite:///investor.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Paths to your CSV files
    companies_path = "test/companies.csv"
    financial_path = "test/financial.csv"

    # Load data from CSV files using the helper function.
    add_dictionary(Financial, read_csv_as_dict(financial_path), session)
    add_dictionary(Companies, read_csv_as_dict(companies_path), session)

    session.commit()
    print("Database created successfully!")

if __name__ == '__main__':
    main()