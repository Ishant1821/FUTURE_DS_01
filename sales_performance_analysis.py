import pandas as pd

# 1. Load the raw dataset 
# (Using the exact KaggleHub path used in the Power BI ETL pipeline)
file_path = r"C:\Users\i0240\.cache\kagglehub\datasets\ulrikthygepedersen\online-retail-dataset\versions\2\online_retail.csv"
df = pd.read_csv(file_path)

# 2. Data Cleaning
# Drop rows where CustomerID is missing to ensure data integrity
df_clean = df.dropna(subset=['CustomerID']).copy()

# Filter out cancellations, negative quantities, and zero prices
df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]

# 3. Data Transformation
# Ensure InvoiceDate is a proper datetime object for time-series analysis
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])

# Create the Total Revenue column 
df_clean['Total Revenue'] = df_clean['Quantity'] * df_clean['UnitPrice']

# 4. Pipeline Verification Output
print("--- Data Cleaning Pipeline Complete ---")
print(f"Total Rows Cleaned & Kept: {len(df_clean):,}")
print(f"Total Sales Revenue Processed: ${df_clean['Total Revenue'].sum():,.2f}")
print("Ready for Power BI Integration.")
