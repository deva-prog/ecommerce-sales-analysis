# ==============================
# DATASET 1 - SALES ANALYSIS
# ==============================
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------
# Dataset1 Loading
# -----------------------------
df1 = pd.read_csv("data/Ecommerce_Sales_Prediction_Dataset1.csv")
print("Dataset 1 Preview:")
print("original shape:",df1.shape)
print("duplicate values:",df1.duplicated().sum())
print("missing value:",df1.isnull().sum())
# -----------------------------
# Feature Engineering
# -----------------------------
df1["Revenue"]=(df1["Price"]-df1["Discount"]) * df1["Units_Sold"]
print("\nRevenue column added successfully:")
print(df1.head())
print("\nColumns after adding Revenue:")
print(df1.columns)
# -----------------------------
# KPI Analysis
# -----------------------------
total_revenue = df1["Revenue"].sum()
print("Total Revenue:", total_revenue)
avg_revenue = df1["Revenue"].mean()
print("Average Revenue per order:", avg_revenue)
total_units = df1["Units_Sold"].sum()
print("total units sold:",total_units)
# -----------------------------
# Monthly Trend Analysis
# -----------------------------
df1["Date"] = pd.to_datetime(df1["Date"],dayfirst=True)
print(df1.dtypes)
df1["month"] = df1["Date"].dt.month
monthly_revenue = df1.groupby("month")["Revenue"].sum()
print("\nMonthly Revenue:", monthly_revenue)
plt.figure(figsize=(8,5))
monthly_revenue.plot(kind = "line",marker ="o" )
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
# -----------------------------
# Category Analysis
# -----------------------------
category_revenue = df1.groupby("Product_Category")["Revenue"].sum().sort_values(ascending = False)
print("\nCategory Revenue:", category_revenue)
plt.figure(figsize=(8,5))
category_revenue.plot(kind = "bar")
plt.title("Revenue by product category")
plt.xlabel("Product Category")
plt.ylabel("Revenue")
plt.xticks(rotation = 0)
plt.show()

segment_revenue = df1.groupby("Customer_Segment")["Revenue"].sum().sort_values(ascending=False)
print("\nSegment Revenue:", segment_revenue)
plt.figure(figsize=(8,5))
segment_revenue.plot(kind="bar")
plt.title("revenue by customer segment")
plt.xlabel("customer segment")
plt.ylabel("Revenue")
plt.xticks(rotation = 0)
plt.show()
# -----------------------------
# Marketing Impact Analysis
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df1["Marketing_Spend"],df1["Revenue"])
plt.title("Marketing Spend vs Revenue")
plt.ylabel("Revenue")
plt.xlabel("marketing spend")
plt.show()
#calculate correlation
correlation=df1["Marketing_Spend"].corr(df1["Revenue"])
print("correlation between marketing spend and revenue:",correlation)
print("\nProject Insights:")
print("1. Sports category generates highest revenue.")
print("2. Premium customers contribute the most revenue.")
print("3. Marketing spend shows almost no correlation with revenue (very weak relationship).")

df1.to_csv("clean_sales_data.csv", index=False)
















