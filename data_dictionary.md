# Mutual Fund Analytics Data Dictionary

## Project Overview

This document describes the datasets used in the Mutual Fund Analytics project. It includes the data source, column names, data types, and business definitions for each dataset.

---

# Dataset Information

## Dataset 1: 01_fund_master.csv

**Purpose:** Contains master information about all mutual fund schemes.

**Source:** AMFI Dataset

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| amfi_code | Integer | Unique AMFI scheme identifier |
| fund_house | Text | Name of the mutual fund company |
| scheme_name | Text | Mutual fund scheme name |
| category | Text | Main fund category |
| sub_category | Text | Sub-category of the scheme |
| plan | Text | Direct or Regular plan |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Annual expense ratio (%) |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP investment amount |
| min_lumpsum_amount | Integer | Minimum lump sum investment |
| fund_manager | Text | Name of the fund manager |
| risk_category | Text | Investment risk category |
| sebi_category_code | Text | SEBI category code |

---

## Dataset 2: 02_nav_history.csv

**Purpose:** Stores historical NAV values of mutual fund schemes.

**Source:** MFAPI / AMFI

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| amfi_code | Integer | AMFI scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## Dataset 3: 03_aum_by_fund_house.csv

**Purpose:** Assets Under Management by fund house.

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| date | Date | Reporting date |
| fund_house | Text | Mutual fund company |
| aum_lakh_crore | Float | AUM in lakh crore |
| aum_crore | Integer | AUM in crore |
| num_schemes | Integer | Number of schemes managed |

---

## Dataset 4: 04_monthly_sip_inflows.csv

**Purpose:** Monthly SIP investment statistics.

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| month | Date | Reporting month |
| sip_inflow_crore | Integer | SIP inflow amount |
| active_sip_accounts_crore | Float | Active SIP accounts |
| new_sip_accounts_lakh | Float | Newly opened SIP accounts |
| sip_aum_lakh_crore | Float | SIP Assets Under Management |
| yoy_growth_pct | Float | Year-over-Year growth percentage |

---

## Dataset 5: 05_category_inflows.csv

**Purpose:** Monthly category-wise inflows.

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| month | Date | Reporting month |
| category | Text | Mutual fund category |
| net_inflow_crore | Float | Net inflow amount |

---

## Dataset 6: 06_industry_folio_count.csv

**Purpose:** Industry-wise folio statistics.

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| month | Date | Reporting month |
| total_folios_crore | Float | Total folios |
| equity_folios_crore | Float | Equity folios |
| debt_folios_crore | Float | Debt folios |
| hybrid_folios_crore | Float | Hybrid folios |
| others_folios_crore | Float | Other folios |

---

## Dataset 7: 07_scheme_performance.csv

**Purpose:** Performance metrics for mutual fund schemes.

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| amfi_code | Integer | AMFI scheme code |
| scheme_name | Text | Scheme name |
| fund_house | Text | Fund house |
| category | Text | Scheme category |
| plan | Text | Direct or Regular plan |
| return_1yr_pct | Float | 1-Year return |
| return_3yr_pct | Float | 3-Year return |
| return_5yr_pct | Float | 5-Year return |
| benchmark_3yr_pct | Float | Benchmark return |
| alpha | Float | Alpha value |
| beta | Float | Beta value |
| sharpe_ratio | Float | Sharpe ratio |
| sortino_ratio | Float | Sortino ratio |
| std_dev_ann_pct | Float | Annual standard deviation |
| max_drawdown_pct | Float | Maximum drawdown |
| aum_crore | Integer | Assets under management |
| expense_ratio_pct | Float | Expense ratio |
| morningstar_rating | Integer | Morningstar rating |
| risk_grade | Text | Risk grade |

---

## Dataset 8: 08_investor_transactions.csv

**Purpose:** Investor transaction records.

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| investor_id | Text | Unique investor ID |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Scheme code |
| transaction_type | Text | SIP, Lumpsum or Redemption |
| amount_inr | Float | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | City tier |
| age_group | Text | Investor age group |
| gender | Text | Investor gender |
| annual_income_lakh | Float | Annual income |
| payment_mode | Text | Payment method |
| kyc_status | Text | KYC verification status |

---

## Dataset 9: 09_portfolio_holdings.csv

**Purpose:** Portfolio holdings of mutual fund schemes.

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| amfi_code | Integer | Scheme code |
| stock_symbol | Text | Stock ticker |
| stock_name | Text | Company name |
| sector | Text | Industry sector |
| weight_pct | Float | Portfolio weight |
| market_value_cr | Float | Market value |
| current_price_inr | Float | Current stock price |
| portfolio_date | Date | Portfolio date |

---

## Dataset 10: 10_benchmark_indices.csv

**Purpose:** Historical benchmark index values.

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| date | Date | Trading date |
| index_name | Text | Benchmark index name |
| close_value | Float | Closing value of the index |

---

# Data Cleaning Performed

- Removed duplicate records.
- Converted date columns to datetime format.
- Standardized transaction type values.
- Validated NAV values greater than zero.
- Validated positive transaction amounts.
- Verified expense ratio between 0.1% and 2.5%.
- Saved cleaned datasets in the `data/processed` folder.

---

# Database Information

**Database Name:** bluestock_mf.db

**Database Type:** SQLite

## Dimension Tables
- dim_fund
- dim_date

## Fact Tables
- fact_nav
- fact_transactions
- fact_performance
- fact_aum