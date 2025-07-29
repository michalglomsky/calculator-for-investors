# Calculator for Investors 📈
A program from Python Developer course on hyperskill.org.

## 📌 Overview

A simple, console-based Python program for managing and analyzing financial data of stock market companies. The application uses an SQLite database to store information, which is initially imported from CSV files. The user can interact with the program through an intuitive menu in the terminal.

-----

## 🚀 Installation and Setup

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-address>
    cd <project-folder-name>
    ```

2.  **Prepare the initial data files:**
    For the first run only, ensure that `companies.csv` and `financial.csv` are located inside a `test/` directory.

3.  **Install dependencies:**
    This project requires **SQLAlchemy** (for database interaction) and **Pandas** (for data manipulation).

    ```bash
    pip install sqlalchemy pandas
    ```

4.  **Run the program:**
    Execute the following command in your terminal:

    ```bash
    python main.py
    ```

    On its first execution, the program will read the CSV files and create `investor.db`. Afterwards, all data will be read from and saved to `investor.db`.

-----

## 📂 Project Structure

The directory structure, including the database file generated after the first run, is as follows:

```
.
├── main.py        # Your main Python script
├── investor.db    # The SQLite database for data persistence
└── test/
    ├── companies.csv
    └── financial.csv
```

-----

## 🗃️ Database Structure

The `investor.db` database consists of two tables: `companies` and `financial`, which store general and financial data respectively.

  * **`companies` table**: `ticker` (Primary Key), `name`, `sector`.
  * **`financial` table**: `ticker` (Primary Key), `ebitda`, `sales`, `net_profit`, etc.

-----

## 📖 How It Works

The program is operated via a text-based menu in the console, allowing for full CRUD (Create, Read, Update, Delete) operations and financial analysis on the company data stored in the database.

### Main Menu

```
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria
```

### CRUD Operations

```
CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies
```

### Top 10 Companies

```
TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA
```

