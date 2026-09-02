import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

num_deals = 1000

industries = [
    "Technology",
    "Finance",
    "Healthcare",
    "Retail",
    "Education",
    "Manufacturing"
]

sales_reps = [
    "Rahul",
    "Priya",
    "Arjun",
    "Sneha",
    "Vikram",
    "Ananya"
]

lead_sources = [
    "Website",
    "Referral",
    "LinkedIn",
    "Email Campaign",
    "Cold Call",
    "Partner"
]

deal_stages = [
    "Prospecting",
    "Qualification",
    "Proposal",
    "Negotiation",
    "Closed Won",
    "Closed Lost"
]

data = []

start_date = datetime(2025, 1, 1)

for i in range(num_deals):

    created_date = start_date + timedelta(
        days=np.random.randint(0, 600)
    )

    deal_value = np.random.randint(50000, 5000000)

    stage = np.random.choice(
        deal_stages,
        p=[0.20, 0.20, 0.20, 0.15, 0.15, 0.10]
    )

    probability_map = {
        "Prospecting": 0.10,
        "Qualification": 0.25,
        "Proposal": 0.50,
        "Negotiation": 0.75,
        "Closed Won": 1.00,
        "Closed Lost": 0.00
    }

    probability = probability_map[stage]

    expected_close_date = created_date + timedelta(
        days=np.random.randint(15, 180)
    )

    if stage in ["Closed Won", "Closed Lost"]:
        actual_close_date = expected_close_date
    else:
        actual_close_date = None

    if stage == "Closed Won":
        status = "Won"
    elif stage == "Closed Lost":
        status = "Lost"
    else:
        status = "Open"

    data.append([
        f"DEAL-{i+1:04d}",
        f"Company {i+1}",
        np.random.choice(industries),
        np.random.choice(sales_reps),
        np.random.choice(lead_sources),
        stage,
        deal_value,
        probability,
        created_date,
        expected_close_date,
        actual_close_date,
        status
    ])

columns = [
    "deal_id",
    "company",
    "industry",
    "sales_rep",
    "lead_source",
    "deal_stage",
    "deal_value",
    "probability",
    "created_date",
    "expected_close_date",
    "actual_close_date",
    "status"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data/crm_sales_data.csv", index=False)

print("Dataset created successfully!")
print("Number of deals:", len(df))
print(df.head())