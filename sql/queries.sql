-- ==========================================
-- 1. Top 5 Funds by AUM
-- ==========================================

SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- ==========================================
-- 2. Average NAV per Month
-- ==========================================

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- ==========================================
-- 3. Monthly SIP Inflow
-- ==========================================

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM sip_inflows
ORDER BY month;

-- ==========================================
-- 4. Transactions by State
-- ==========================================

SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- ==========================================
-- 5. Funds with Expense Ratio < 1%
-- ==========================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- ==========================================
-- 6. Top 10 Funds by 5-Year Return
-- ==========================================

SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- ==========================================
-- 7. Average Expense Ratio by Category
-- ==========================================

SELECT
    category,
    AVG(expense_ratio_pct) AS avg_expense
FROM fact_performance
GROUP BY category;

-- ==========================================
-- 8. Top 10 Cities by Investment Amount
-- ==========================================

SELECT
    city,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY city
ORDER BY total_investment DESC
LIMIT 10;

-- 9. Number of Investors by G

SELECT
    gender,
    COUNT(DISTINCT investor_id) AS investors
FROM fact_transactions
GROUP BY gender;


SELECT
    scheme_name,
    alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 10;