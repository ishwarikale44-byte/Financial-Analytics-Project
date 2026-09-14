import pandas as pd
import matplotlib.pyplot as plt

# Load the financial data
df = pd.read_csv("transactions.csv")

print("\n========== FINANCIAL DATA ==========\n")
print(df)

# Convert Date into date format
df["Date"] = pd.to_datetime(df["Date"])

# Total Income
total_income = df[df["Type"] == "Income"]["Amount"].sum()

# Total Expense
total_expense = df[df["Type"] == "Expense"]["Amount"].sum()

# Net Savings
net_savings = total_income - total_expense

print("\n========== FINANCIAL SUMMARY ==========")
print("Total Income :", total_income)
print("Total Expense:", total_expense)
print("Net Savings  :", net_savings)

# Expense data
expense_data = df[df["Type"] == "Expense"]

# Expense by Category
category_expense = (
    expense_data
    .groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== EXPENSE BY CATEGORY ==========")
print(category_expense)

# Create Month column
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Monthly Income
monthly_income = (
    df[df["Type"] == "Income"]
    .groupby("Month")["Amount"]
    .sum()
)

# Monthly Expense
monthly_expense = (
    df[df["Type"] == "Expense"]
    .groupby("Month")["Amount"]
    .sum()
)

# Monthly Analysis
monthly_analysis = pd.DataFrame({
    "Income": monthly_income,
    "Expense": monthly_expense
}).fillna(0)

monthly_analysis["Savings"] = (
    monthly_analysis["Income"]
    - monthly_analysis["Expense"]
)

print("\n========== MONTHLY ANALYSIS ==========")
print(monthly_analysis)

# Expense Chart
plt.figure(figsize=(10, 6))
category_expense.plot(kind="bar")

plt.title("Expense by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()

plt.savefig("spending_by_category.png")
plt.show()

# Monthly Cash Flow Chart
monthly_analysis.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Monthly Income, Expense and Savings")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.tight_layout()

plt.savefig("monthly_cashflow.png")
plt.show()

print("\n====================================")
print("Analysis completed successfully!")
print("====================================")