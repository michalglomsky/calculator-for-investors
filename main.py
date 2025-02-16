import csv
import os
from sqlalchemy import create_engine, Column, Float, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


def convert_value(column, value):
    """
    Convert the input value to the type expected by the given SQLAlchemy column.
    Treats empty strings as None.
    """
    if value == "":
        return None

    if isinstance(column.type, Integer):
        return int(value)
    elif isinstance(column.type, Float):
        return float(value)
    elif isinstance(column.type, String):
        return str(value)
    else:
        return value


def load_csv(model, file_path, session):
    """
    Reads a CSV file and maps each row to an instance of the given model.

    :param model: The SQLAlchemy model class.
    :param file_path: Path to the CSV file.
    :param session: SQLAlchemy session.
    """
    with open(file_path, encoding='utf-8') as csv_file:
        csv_dictionary = csv.DictReader(csv_file)
        for row in csv_dictionary:
            instance = model()  # Create a new instance of the model
            for key, value in row.items():
                # Get the corresponding column from the model
                column = model.__table__.columns.get(key)
                if column is not None:
                    converted_value = convert_value(column, value)
                    setattr(instance, key, converted_value)
            session.add(instance)


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
    db_path = "investor.db"
    if os.path.exists(db_path):
        os.remove(db_path)

    engine = create_engine('sqlite:///investor.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Paths to your CSV files
    companies_path = "test/companies.csv"
    financial_path = "test/financial.csv"

    # Load data from CSV files using the helper function.
    load_csv(Financial, financial_path, session)
    load_csv(Companies, companies_path, session)

    session.commit()
    session.close()
    print("Database created successfully!")


if __name__ == '__main__':
    main()
