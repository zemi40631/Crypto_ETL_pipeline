import requests
import pandas as pd
from sqlalchemy import create_engine


# Step 1: Extract Data from CoinGecko API
def extract_data():
    """Fetch cryptocurrency data from the CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("Data extraction successful.")
        return response.json()
    else:
        print(f"Failed to extract data. Status code: {response.status_code}")
        return []


# Step 2: Transform Data using Pandas
def transform_data(data):
    """Transform the raw JSON data into a structured format."""
    df = pd.DataFrame(data)
    transformed_data = df[["id", "name", "symbol", "current_price", "market_cap", "total_volume"]]
    transformed_data.loc[:, "current_price"] = transformed_data["current_price"].round(2)  # Round prices to 2 decimals
    print("Data transformation complete.")
    return transformed_data


# Step 3: Load Data into MySQL
def load_data_to_mysql(transformed_data):
    """Load the transformed data into a MySQL database."""
    try:
        # Replace 'your_username', 'your_password', and 'your_database' with your MySQL credentials
        engine = create_engine("mysql+pymysql://root:bugbutt5@localhost:3306/db")

        # Load the data into the 'crypto_prices' table (replace table if it exists)
        transformed_data.to_sql("crypto_prices", engine, if_exists="replace", index=True)
        print("Data loaded into MySQL successfully.")

    except Exception as e:
        print(f"Failed to load data into MySQL: {e}")


# Main function to run the ETL process
def run_etl():
    """Run the full ETL pipeline."""
    print("Starting ETL process...")
    data = extract_data()
    if data:
        transformed_data = transform_data(data)
        load_data_to_mysql(transformed_data)
    print("ETL process completed.")


# Run the ETL pipeline
if __name__ == "__main__":
    run_etl()
