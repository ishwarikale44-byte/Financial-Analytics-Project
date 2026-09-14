import sqlite3

conn = sqlite3.connect("financial_analytics.db")

result = conn.execute("""
SELECT Category, SUM(Amount) AS Total_Expense
FROM transactions
WHERE Type = 'Expense'
GROUP BY Category
ORDER BY Total_Expense DESC
""").fetchall()

print("Category-wise Expenses:")
for row in result:
    print(row[0], "=", row[1])

conn.close()