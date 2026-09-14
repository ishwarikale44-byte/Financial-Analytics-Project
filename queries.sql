-- 1. Total Income
SELECT SUM(Amount) AS Total_Income
FROM transactions
WHERE Type = 'Income';


-- 2. Total Expense
SELECT SUM(Amount) AS Total_Expense
FROM transactions
WHERE Type = 'Expense';


-- 3. Expense by Category
SELECT 
    Category,
    SUM(Amount) AS Total_Expense
FROM transactions
WHERE Type = 'Expense'
GROUP BY Category
ORDER BY Total_Expense DESC;


-- 4. Monthly Income
SELECT 
    strftime('%Y-%m', Date) AS Month,
    SUM(Amount) AS Monthly_Income
FROM transactions
WHERE Type = 'Income'
GROUP BY Month
ORDER BY Month;


-- 5. Monthly Expense
SELECT 
    strftime('%Y-%m', Date) AS Month,
    SUM(Amount) AS Monthly_Expense
FROM transactions
WHERE Type = 'Expense'
GROUP BY Month
ORDER BY Month;