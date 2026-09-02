import pandas as pd

df = pd.read_csv("data/processed_sales_data.csv")

total_pipeline = df[df["status"] == "Open"]["deal_value"].sum()

expected_revenue = df["expected_revenue"].sum()

won_revenue = df[df["status"] == "Won"]["deal_value"].sum()

total_closed = df[
    df["status"].isin(["Won", "Lost"])
].shape[0]

won_deals = df[df["status"] == "Won"].shape[0]

win_rate = won_deals / total_closed * 100

average_deal = df["deal_value"].mean()

print("========== SALES ANALYTICS ==========")

print(f"Total Pipeline: ₹{total_pipeline:,.0f}")

print(f"Expected Revenue: ₹{expected_revenue:,.0f}")

print(f"Won Revenue: ₹{won_revenue:,.0f}")

print(f"Win Rate: {win_rate:.2f}%")

print(f"Average Deal Size: ₹{average_deal:,.0f}")