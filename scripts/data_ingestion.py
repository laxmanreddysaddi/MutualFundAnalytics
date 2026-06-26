import os
import pandas as pd

# Path to the raw data folder
data_folder = "data/raw"

# Get all CSV files from the folder
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

print("=" * 80)
print("CSV Files Found:")
print(csv_files)
print("=" * 80)

# Read each CSV file
for file in csv_files:

    file_path = os.path.join(data_folder, file)

    try:
        # Read CSV
        df = pd.read_csv(file_path)

        print("\n" + "=" * 80)
        print(f"Dataset: {file}")
        print("=" * 80)

        # Shape
        print("\nShape:")
        print(df.shape)

        # Data Types
        print("\nData Types:")
        print(df.dtypes)

        # First 5 Rows
        print("\nFirst 5 Rows:")
        print(df.head())

        # Column Names
        print("\nColumn Names:")
        print(df.columns.tolist())

        # Missing Values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # Duplicate Rows
        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        # Summary Statistics
        print("\nSummary Statistics:")
        print(df.describe(include='all'))

        print("\n" + "-" * 80)
        print("Data Quality Summary")

        if df.isnull().sum().sum() == 0:
            print("✔ No Missing Values")
        else:
            print(f"⚠ Missing Values Found: {df.isnull().sum().sum()}")

        duplicates = df.duplicated().sum()

        if duplicates == 0:
            print("✔ No Duplicate Rows")
        else:
            print(f"⚠ Duplicate Rows Found: {duplicates}")

        print(f"✔ Total Rows    : {df.shape[0]}")
        print(f"✔ Total Columns : {df.shape[1]}")

        print("-" * 80)

    except Exception as e:
        print(f"\nError reading {file}")
        print(e)
print("\n" + "=" * 80)
print("FUND MASTER EXPLORATION")
print("=" * 80)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())
print("\n" + "=" * 80)
print("AMFI CODE VALIDATION")
print("=" * 80)

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

if len(missing_codes) == 0:
    print("✅ All AMFI codes in fund_master exist in nav_history.")
else:
    print("❌ Missing AMFI Codes:")
    print(missing_codes)

print(f"\nTotal Fund Master Codes : {len(fund_codes)}")
print(f"Total NAV History Codes : {len(nav_codes)}")