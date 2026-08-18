"""
generate_dataset.py
--------------------
Generates a realistic retail/e-commerce sales dataset for the
Retail Sales & Customer Analytics NumPy project.

Run this once to (re)create data/retail_sales.csv.
The dataset intentionally contains beginner-level data-quality
issues (missing values, duplicates, negative numbers, bad dates,
extra spaces, inconsistent category text) so students get real
practice cleaning data before analysis.
"""

import numpy as np
import csv
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

N_ROWS = 2000

# ---------------------------------------------------------------
# Reference data
# ---------------------------------------------------------------
categories_products = {
    "Electronics": ["Wireless Mouse", "Bluetooth Speaker", "USB-C Charger",
                     "Laptop Stand", "Webcam HD", "Power Bank 10000mAh"],
    "Clothing": ["Men Cotton T-Shirt", "Women Kurti", "Denim Jeans",
                 "Winter Jacket", "Running Shoes", "Formal Shirt"],
    "Home & Kitchen": ["Non-Stick Pan", "Storage Container Set",
                       "LED Table Lamp", "Ceramic Mug Set", "Steel Water Bottle"],
    "Beauty": ["Face Wash", "Moisturizer Cream", "Lipstick", "Sunscreen SPF50",
               "Hair Serum"],
    "Sports": ["Yoga Mat", "Cricket Bat", "Football", "Dumbbell Set 5kg",
               "Skipping Rope"],
    "Books": ["Fiction Novel", "Self Help Book", "Children Story Book",
              "Cook Book"],
    "Grocery": ["Basmati Rice 5kg", "Cooking Oil 1L", "Green Tea Pack",
                "Almonds 500g"],
}

# Note some categories written inconsistently on purpose (cleaning practice)
category_variants = {
    "Electronics": ["Electronics", "electronics", "ELECTRONICS", " Electronics"],
    "Clothing": ["Clothing", "clothing", "Cloths", " Clothing "],
    "Home & Kitchen": ["Home & Kitchen", "home & kitchen", "Home and Kitchen"],
    "Beauty": ["Beauty", "beauty", " Beauty"],
    "Sports": ["Sports", "sports", "SPORTS"],
    "Books": ["Books", "books"],
    "Grocery": ["Grocery", "grocery", " Grocery"],
}

city_region_state = [
    ("Mumbai", "Maharashtra", "West"), ("Pune", "Maharashtra", "West"),
    ("Delhi", "Delhi", "North"), ("Noida", "Uttar Pradesh", "North"),
    ("Lucknow", "Uttar Pradesh", "North"), ("Jaipur", "Rajasthan", "North"),
    ("Bengaluru", "Karnataka", "South"), ("Chennai", "Tamil Nadu", "South"),
    ("Hyderabad", "Telangana", "South"), ("Kolkata", "West Bengal", "East"),
    ("Patna", "Bihar", "East"), ("Bhubaneswar", "Odisha", "East"),
    ("Ahmedabad", "Gujarat", "West"), ("Indore", "Madhya Pradesh", "Central"),
    ("Bhopal", "Madhya Pradesh", "Central"),
]

payment_modes = ["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash on Delivery"]
customer_types = ["New", "Returning"]

first_names = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh",
               "Ishaan", "Kabir", "Ananya", "Diya", "Isha", "Kavya", "Myra",
               "Riya", "Saanvi", "Aadhya", "Priya", "Rohit", "Neha", "Karan",
               "Simran", "Rahul", "Pooja"]
last_names = ["Sharma", "Verma", "Gupta", "Singh", "Kumar", "Mehta", "Reddy",
              "Nair", "Iyer", "Das", "Patel", "Chauhan", "Yadav", "Kapoor"]

# ---------------------------------------------------------------
# Build customer pool (so some customers repeat -> repeat-customer analysis)
# ---------------------------------------------------------------
N_CUSTOMERS = 550
customers = []
for i in range(1, N_CUSTOMERS + 1):
    cid = f"CUST{i:04d}"
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    customers.append((cid, name))

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
date_range_days = (end_date - start_date).days

rows = []
header = ["Order_ID", "Order_Date", "Customer_ID", "Customer_Name", "City",
          "State", "Region", "Category", "Product", "Quantity", "Unit_Price",
          "Discount", "Sales", "Cost", "Profit", "Payment_Mode", "Customer_Type"]

for i in range(1, N_ROWS + 1):
    order_id = f"ORD{i:05d}"

    # ---- Order_Date: mostly valid, some intentionally malformed ----
    rand_day = random.randint(0, date_range_days)
    order_date_obj = start_date + timedelta(days=rand_day)
    bad_date_roll = random.random()
    if bad_date_roll < 0.01:
        order_date = ""  # missing date
    elif bad_date_roll < 0.02:
        order_date = "2024-13-40"  # invalid date
    else:
        order_date = order_date_obj.strftime("%Y-%m-%d")

    cust_id, cust_name = random.choice(customers)

    city, state, region = random.choice(city_region_state)

    category_clean = random.choice(list(categories_products.keys()))
    category = random.choice(category_variants[category_clean])
    product = random.choice(categories_products[category_clean])

    # ---- Quantity: occasionally invalid/negative/missing ----
    qty_roll = random.random()
    if qty_roll < 0.015:
        quantity = -random.randint(1, 3)          # invalid negative qty
    elif qty_roll < 0.03:
        quantity = ""                              # missing qty
    else:
        quantity = random.randint(1, 8)

    # ---- Unit price by category (rough realistic ranges) ----
    price_ranges = {
        "Electronics": (299, 2999), "Clothing": (299, 1999),
        "Home & Kitchen": (199, 1499), "Beauty": (99, 899),
        "Sports": (199, 2499), "Books": (149, 699), "Grocery": (99, 999),
    }
    low, high = price_ranges[category_clean]
    unit_price = round(random.uniform(low, high), 2)
    if random.random() < 0.01:
        unit_price = ""  # missing price

    discount = round(random.choice([0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25]), 2)

    # ---- Compute Sales/Cost/Profit only when quantity & price are valid ----
    if quantity not in ("",) and unit_price != "" and (isinstance(quantity, int)) and quantity > 0:
        gross = quantity * unit_price
        sales = round(gross * (1 - discount), 2)
        cost = round(sales * random.uniform(0.55, 0.8), 2)
        profit = round(sales - cost, 2)
    else:
        sales, cost, profit = "", "", ""

    payment_mode = random.choice(payment_modes)
    customer_type = random.choice(customer_types)

    # ---- Extra whitespace injected on purpose (cleaning practice) ----
    if random.random() < 0.03:
        cust_name = f"  {cust_name}  "
    if random.random() < 0.03:
        city = f" {city}"

    rows.append([order_id, order_date, cust_id, cust_name, city, state,
                 region, category, product, quantity, unit_price, discount,
                 sales, cost, profit, payment_mode, customer_type])

# ---------------------------------------------------------------
# Inject duplicate Order_IDs on purpose (about 15 duplicates)
# ---------------------------------------------------------------
for _ in range(15):
    dup_row = random.choice(rows).copy()
    rows.append(dup_row)

random.shuffle(rows)

with open("/home/claude/retail-sales-numpy-analysis/data/retail_sales.csv",
          "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Generated {len(rows)} rows -> data/retail_sales.csv")
