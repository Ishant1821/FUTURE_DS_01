import os
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

# 1. Download and load the dataset
print("Downloading dataset...")
path = kagglehub.dataset_download("ulrikthygepedersen/online-retail-dataset")
csv_file = [f for f in os.listdir(path) if f.endswith(".csv")][0]

df = pd.read_csv(os.path.join(path, csv_file))
print("Data loaded successfully!")

# 2. Clean the data
df = df.dropna(subset=["CustomerID"])
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# 3. Calculate total revenue
df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']
total_sales = df['TotalRevenue'].sum()
print(f"\nTotal Sales Revenue: ${total_sales:,.2f}")

# 4. Find top products
print("\nTop 5 Products by Revenue:")
print(df.groupby('Description')['TotalRevenue'].sum().nlargest(5))

# 5. Plot and save monthly revenue trend
df['YearMonth'] = df['InvoiceDate'].dt.to_period('M')
monthly_revenue = df.groupby('YearMonth')['TotalRevenue'].sum()
monthly_revenue.index = monthly_revenue.index.astype(str)

plt.figure(figsize=(10, 5))
monthly_revenue.plot(kind="line", marker="o", color="b", linewidth=2)
plt.title("Monthly Revenue Trend", fontsize=14, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Revenue ($)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_revenue_trend.png", dpi=300)
plt.show()