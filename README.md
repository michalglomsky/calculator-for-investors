# Calculator for Investors 📈
A program from Python Developer course on hyperskill.org.

## 📌 Overview

A simple, console-based Python program for managing and analyzing financial data of stock market companies. The application uses an SQLite database to store information, which is initially imported from CSV files. The user can interact with the program through an intuitive menu in the terminal.

-----

## 📋 Features

  * **Data Import**: Automatically creates and populates the `investor.db` database from `companies.csv` and `financial.csv` files on the first run.
  * **CRUD Operations**: Full support for Creating, Reading, Updating, and Deleting company data.
  * **Company Search**: Easily find companies by a partial name search.
  * **Financial Analysis**: Automatically calculates and displays key financial ratios for a selected company, such as:
      * $P/E$ (Price to Earnings)
      * $P/S$ (Price to Sales)
      * $P/B$ (Price to Book)
      * $ND/EBITDA$ (Net Debt to EBITDA)
      * $ROE$ (Return on Equity)
      * $ROA$ (Return on Assets)
      * $L/A$ (Liabilities to Assets)
  * **"Top 10" Rankings**: Displays the top 10 companies based on the following criteria:
      * $ND/EBITDA$
      * $ROE$
      * $ROA$

-----

## 🚀 Installation and Setup

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-address>
    cd <project-folder-name>
    ```

2.  **Prepare the data files:**
    Ensure that the `companies.csv` and `financial.csv` files are located inside a `test/` directory.

3.  **Install dependencies:**
    This project requires the **SQLAlchemy** library. Install it using pip:

    ```bash
    pip install sqlalchemy
    ```

4.  **Run the program:**
    Execute the following command in your terminal:

    ```bash
    python main.py
    ```

    On the first run, the program will automatically create the `investor.db` database file and import the data from your CSV files.

-----

## 📂 Project Structure

The directory structure should look like this for the program to work correctly:

```
.
├── main.py        # Your main Python script
└── test/
    ├── companies.csv
    └── financial.csv
```

-----

## 🗃️ Database Structure

The `investor.db` database consists of two tables:

1.  **`companies`**: Stores basic information about the companies.
    | Column | Type | Description |
    | :--- | :--- | :--- |
    | `ticker` | String | A unique company identifier (Primary Key). |
    | `name` | String | The full name of the company. |
    | `sector` | String | The industry sector in which the company operates. |

2.  **`financial`**: Stores the financial data for the companies.
    | Column | Type | Description |
    | :--- | :--- | :--- |
    | `ticker` | String | The company identifier (Primary Key). |
    | `ebitda` | Float | Earnings Before Interest, Taxes, Depreciation, and Amortization. |
    | `sales` | Float | Revenue from sales. |
    | `net_profit` | Float | Net profit. |
    | `market_price`| Float | Market capitalization. |
    | `net_debt` | Float | Net debt. |
    | `assets` | Float | Total value of assets. |
    | `equity` | Float | Shareholder's equity. |
    | `cash_equivalents`| Float | Cash and cash equivalents. |
    | `liabilities`| Float | Total liabilities. |

-----

## 📖 How It Works

The program is operated via a text-based menu in the console.

### Main Menu

```
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria
```

  * **`0 Exit`**: Terminates the program.
  * **`1 CRUD operations`**: Navigates to the data management menu.
  * **`2 Show top ten companies by criteria`**: Navigates to the rankings menu.

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

  * **`1 Create a company`**: Guides the user through the process of adding a new company and its financial data.
  * **`2 Read a company`**: After searching for and selecting a company, it displays its ticker, name, and calculated financial ratios.
  * **`3 Update a company`**: Allows for the modification of an existing company's financial data.
  * **`4 Delete a company`**: Removes a company and its financial data from the database.
  * **`5 List all companies`**: Displays a list of all companies in the database, sorted alphabetically by ticker.

### Top 10 Companies

```
TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA
```

  * **`1 List by ND/EBITDA`**: Displays the 10 companies with the highest $ND/EBITDA$ ratio.
  * **`2 List by ROE`**: Displays the 10 companies with the highest $ROE$ ratio.
  * **`3 List by ROA`**: Displays the 10 companies with the highest $ROA$ ratio.
