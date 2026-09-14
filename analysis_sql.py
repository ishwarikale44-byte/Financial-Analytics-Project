import sqlite3

conn = sqlite3.connect("financial_analytics.db")

print("\n===== FINANCIAL ANALYTICS =====")

# 1. Total Income
result = conn.execute("""
SELECT SUM(Amount)
FROM transactions
WHERE Type = 'Income'
""").fetchone()

print("\n1. Total Income =", result[0])


# 2. Total Expense
result = conn.execute("""
SELECT SUM(Amount)
FROM transactions
WHERE Type = 'Expense'
""").fetchone()

print("2. Total Expense =", result[0])


# 3. Net Savings
result = conn.execute("""
SELECT
    SUM(CASE WHEN Type = 'Income' THEN Amount ELSE 0 END)
    -
    SUM(CASE WHEN Type = 'Expense' THEN Amount ELSE 0 END)
FROM transactions
""").fetchone()

print("3. Net Savings =", result[0])


# 4. Category-wise Expense
result = conn.execute("""
SELECT Category, SUM(Amount)
FROM transactions
WHERE Type = 'Expense'
GROUP BY Category
ORDER BY SUM(Amount) DESC
""").fetchall()

print("\n4. Category-wise Expense:")

for row in result:
    print(row[0], "=", row[1])


# 5. Monthly Income
result = conn.execute("""
SELECT strftime('%Y-%m', Date), SUM(Amount)
FROM transactions
WHERE Type = 'Income'
GROUP BY strftime('%Y-%m', Date)
ORDER BY strftime('%Y-%m', Date)
""").fetchall()

print("\n5. Monthly Income:")

for row in result:
    print(row[0], "=", row[1])


# 6. Monthly Expense
result = conn.execute("""
SELECT strftime('%Y-%m', Date), SUM(Amount)
FROM transactions
WHERE Type = 'Expense'
GROUP BY strftime('%Y-%m', Date)
ORDER BY strftime('%Y-%m', Date)
""").fetchall()

print("\n6. Monthly Expense:")

for row in result:
    print(row[0], "=", row[1])


conn.close()

print("\n===== ANALYSIS COMPLETED =====")