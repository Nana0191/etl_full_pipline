# Bank Data ETL Pipeline

## Overview

This project is a simple **ETL (Extract, Transform, Load) pipeline** built with Python as part of my Data Engineering learning journey.

The pipeline extracts data about the **largest banks in the world** from a Wikipedia page, transforms the data into multiple currencies using exchange rates, and loads the processed data into both a CSV file and a SQLite database.

This project helped me understand one of the core workflows in Data Engineering:
**Extract → Transform → Load**

---

## Features

* Extract bank market capitalization data from a webpage using web scraping.
* Clean and structure the extracted data.
* Transform market capitalization values into multiple currencies.
* Save processed data into a CSV file.
* Store data in a SQLite database.
* Execute SQL queries for analysis.
* Log the progress of each ETL stage.

---

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Requests**
* **BeautifulSoup**
* **SQLite3**
* **Datetime**

---

## Project Workflow

### 1. Extract

The project scrapes the largest banks table from Wikipedia using:

* `requests` for fetching webpage content
* `BeautifulSoup` for parsing HTML

Extracted fields:

* Bank Name
* Market Capitalization (USD)

---

### 2. Transform

The extracted market capitalization values are converted into multiple currencies using exchange rates stored in a CSV file.

Currencies include:

* GBP
* EUR
* INR

Transformation uses:

* `pandas`
* `numpy`

---

### 3. Load

The transformed data is stored in:

* **CSV file** (`Largest_banks_data.csv`)
* **SQLite Database** (`Banks.db`)

---

### 4. Query

The project executes SQL queries such as:

* Display all banks
* Calculate average market capitalization in GBP
* Retrieve the first 5 bank names

---

## Project Structure

```bash
Bank_data_project/
│── bank.py
│── exchange_rate.csv
│── Largest_banks_data.csv
│── Banks.db
│── code_log.txt
│── README.md
```


## Example Output

* Extracted bank data table
* Converted currency values
* SQL query results
* Log file showing ETL process steps

---

## What I Learned

Through this project, I improved my understanding of:

* ETL pipelines
* Web scraping
* Data transformation
* Working with CSV files
* SQLite databases
* SQL queries in Python
* Logging workflow progress



Built by **Jumana Akram** as part of my journey to becoming a **Data Engineer** 🚀
