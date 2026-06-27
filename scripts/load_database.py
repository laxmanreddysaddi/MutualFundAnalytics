import os
import pandas as pd
from sqlalchemy import create_engine


# Paths

PROCESSED_FOLDER = "data/processed"

# SQLite Database
DATABASE_NAME = "bluestock_mf.db"

# Create SQLite Engine
engine = create_engine(f"sqlite:///{DATABASE_NAME}")

print("=" * 70)
print("LOADING DATA INTO SQLITE DATABASE")
print("=" * 70)

# CSV files to load
files = {
    "dim_fund": "01_fund_master.csv",
    "fact_nav": "02_nav_history.csv",
    "fact_aum": "03_aum_by_fund_house.csv",
    "sip_inflows": "04_monthly_sip_inflows.csv",
    "category_inflows": "05_category_inflows.csv",
    "industry_folio": "06_industry_folio_count.csv",
    "fact_performance": "07_scheme_performance.csv",
    "fact_transactions": "08_investor_transactions.csv",
    "portfolio_holdings": "09_portfolio_holdings.csv",
    "benchmark_indices": "10_benchmark_indices.csv"
}

# Load each CSV into SQLite
for table_name, file_name in files.items():

    file_path = os.path.join(PROCESSED_FOLDER, file_name)

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✔ Loaded {table_name:<25} Rows : {len(df)}")

print("\nDatabase Created Successfully!")
print(f"Database Name : {DATABASE_NAME}")