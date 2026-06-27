import pandas as pd
import os

# ==============================
# Folder Paths
# ==============================

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

print("=" * 80)
print("DATA CLEANING STARTED")
print("=" * 80)

# ==========================================================
# 1. Clean NAV History
# ==========================================================

print("\nCleaning 02_nav_history.csv...")

nav_df = pd.read_csv(os.path.join(RAW_FOLDER, "02_nav_history.csv"))

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values(["amfi_code", "date"])

duplicate_count = nav_df.duplicated().sum()
nav_df = nav_df.drop_duplicates()

nav_df["nav"] = nav_df.groupby("amfi_code")["nav"].ffill()

invalid_nav = (nav_df["nav"] <= 0).sum()
nav_df = nav_df[nav_df["nav"] > 0]

nav_df.to_csv(
    os.path.join(PROCESSED_FOLDER, "02_nav_history.csv"),
    index=False
)

print("Completed")
print("Rows:", len(nav_df))
print("Duplicates Removed:", duplicate_count)
print("Invalid NAV:", invalid_nav)

# ==========================================================
# 2. Clean Investor Transactions
# ==========================================================

print("\nCleaning 08_investor_transactions.csv...")

txn_df = pd.read_csv(
    os.path.join(RAW_FOLDER, "08_investor_transactions.csv")
)

txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"]
)

duplicate_count = txn_df.duplicated().sum()
txn_df = txn_df.drop_duplicates()

txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .str.strip()
    .str.title()
)

txn_df["transaction_type"] = txn_df["transaction_type"].replace({
    "Sip": "SIP",
    "Lump Sum": "Lumpsum",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

invalid_amount = (txn_df["amount_inr"] <= 0).sum()

txn_df = txn_df[txn_df["amount_inr"] > 0]

valid_kyc = ["Verified", "Pending"]

invalid_kyc = txn_df[
    ~txn_df["kyc_status"].isin(valid_kyc)
]

txn_df.to_csv(
    os.path.join(PROCESSED_FOLDER,
                 "08_investor_transactions.csv"),
    index=False
)

print("Completed")
print("Rows:", len(txn_df))
print("Duplicates Removed:", duplicate_count)
print("Invalid Amount:", invalid_amount)
print("Invalid KYC:", len(invalid_kyc))

# ==========================================================
# 3. Clean Scheme Performance
# ==========================================================

print("\nCleaning 07_scheme_performance.csv...")

performance_df = pd.read_csv(
    os.path.join(RAW_FOLDER, "07_scheme_performance.csv")
)

duplicate_count = performance_df.duplicated().sum()
performance_df = performance_df.drop_duplicates()

numeric_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

for col in numeric_columns:
    performance_df[col] = pd.to_numeric(
        performance_df[col],
        errors="coerce"
    )

missing_numeric = performance_df[
    numeric_columns
].isnull().sum().sum()

expense_anomaly = performance_df[
    (performance_df["expense_ratio_pct"] < 0.1)
    |
    (performance_df["expense_ratio_pct"] > 2.5)
]

performance_df.to_csv(
    os.path.join(PROCESSED_FOLDER,
                 "07_scheme_performance.csv"),
    index=False
)

print("Completed")
print("Rows:", len(performance_df))
print("Duplicates Removed:", duplicate_count)
print("Missing Numeric:", missing_numeric)
print("Expense Ratio Anomalies:", len(expense_anomaly))

# ==========================================================
# 4. Clean Remaining Files
# ==========================================================

remaining_files = [

    "01_fund_master.csv",

    "03_aum_by_fund_house.csv",

    "04_monthly_sip_inflows.csv",

    "05_category_inflows.csv",

    "06_industry_folio_count.csv",

    "09_portfolio_holdings.csv",

    "10_benchmark_indices.csv"

]

print("\nCleaning Remaining Files...")

for file in remaining_files:

    df = pd.read_csv(
        os.path.join(RAW_FOLDER, file)
    )

    df = df.drop_duplicates()

    for column in df.columns:

        if (
            "date" in column.lower()
            or column.lower() == "month"
        ):

            try:
                df[column] = pd.to_datetime(df[column])
            except:
                pass

    df.to_csv(
        os.path.join(PROCESSED_FOLDER, file),
        index=False
    )

    print(file, "Cleaned")

print("\n" + "=" * 80)
print("DATA CLEANING COMPLETED")
print("=" * 80)

print("\nProcessed files saved in:")
