import pandas as pd

# Read transaction data
df = pd.read_csv("transactions.csv")

# Create Excel file
with pd.ExcelWriter("Financial_Analytics_Dashboard.xlsx", engine="openpyxl") as writer:

    # Raw transaction data
    df.to_excel(writer, sheet_name="Transactions", index=False)

    # Summary
    summary = pd.DataFrame({
        "Metric": [
            "Total Income",
            "Total Expense",
            "Net Savings"
        ],
        "Amount": [
            df.loc[df["Type"] == "Income", "Amount"].sum(),
            df.loc[df["Type"] == "Expense", "Amount"].sum(),
            df.loc[df["Type"] == "Income", "Amount"].sum()
            - df.loc[df["Type"] == "Expense", "Amount"].sum()
        ]
    })

    summary.to_excel(writer, sheet_name="Summary", index=False)

    # Category-wise expenses
    category_expense = (
        df[df["Type"] == "Expense"]
        .groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    category_expense.to_excel(
        writer,
        sheet_name="Category Analysis",
        index=False
    )

    # Monthly analysis
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.strftime("%Y-%m")

    monthly = (
        df.groupby(["Month", "Type"])["Amount"]
        .sum()
        .reset_index()
    )

    monthly.to_excel(
        writer,
        sheet_name="Monthly Analysis",
        index=False
    )

print("Excel Dashboard file created successfully!")