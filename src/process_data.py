import pandas as pd

# Load dataset
df = pd.read_csv("data/crm_sales_data.csv")

# Convert dates
df["created_date"] = pd.to_datetime(df["created_date"])
df["expected_close_date"] = pd.to_datetime(df["expected_close_date"])
df["actual_close_date"] = pd.to_datetime(df["actual_close_date"])

# Calculate sales cycle
df["sales_cycle_days"] = (
    df["expected_close_date"] - df["created_date"]
).dt.days

# Calculate expected revenue
df["expected_revenue"] = (
    df["deal_value"] * df["probability"]
)

# Extract quarter
df["quarter"] = df["expected_close_date"].dt.to_period("Q").astype(str)

# Save processed data
df.to_csv(
    "data/processed_sales_data.csv",
    index=False
)

print("Data processing completed!")
print()
print(df.head())