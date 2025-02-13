# Cryptocurrency ETL Pipeline

This project is a simple ETL (Extract, Transform, Load) pipeline that extracts cryptocurrency data from the CoinGecko API, transforms it using Pandas, and loads it into a MySQL database.

## Features
- **Extract**: Fetch the top 100 cryptocurrencies based on market cap from the CoinGecko API.
- **Transform**: Clean and transform the data using Pandas.
- **Load**: Insert the transformed data into a MySQL database.

---

## Prerequisites

1. **Python**: Ensure Python 3.x is installed.  
   Download and install Python from [python.org](https://www.python.org/).  

2. **MySQL Database**: Install MySQL and create a database.  
   [Download MySQL](https://dev.mysql.com/downloads/)  

3. **Python Packages**: Install the required Python packages by running:
   ```bash
   pip install requests pandas sqlalchemy pymysql
    ```