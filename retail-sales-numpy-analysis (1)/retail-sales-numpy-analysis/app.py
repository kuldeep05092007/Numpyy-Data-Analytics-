"""
app.py
-------
Streamlit dashboard for the Retail Sales & Customer Analytics project.

Run locally with:
    streamlit run app.py

This turns the NumPy analysis in src/analysis.py into an interactive
web application - the same KPIs and charts from the notebook, but
filterable by Region, Category, Customer Type, and Payment Mode.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
import numpy as np
import pandas as pd

from data_loader import load_clean_arrays, to_numpy_arrays
from analysis import (
    total_revenue, total_profit, total_quantity, unique_customer_count,
    order_count, average_order_value, profit_margin_percent,
    group_sum, top_n, monthly_totals, repeat_customer_percentage,
)
from visualization import (
    monthly_sales_trend, sales_by_category, profit_by_category,
    top_products, sales_by_region, orders_per_customer_type,
)

st.set_page_config(page_title="Retail Sales Analytics", layout="wide")

st.title("📊 Retail Sales & Customer Analytics Dashboard")
st.caption("Built with Python, NumPy, and Streamlit")

# ---------------------------------------------------------------
# Load and clean data (cached so it isn't repeated on every interaction)
# ---------------------------------------------------------------
@st.cache_data
def get_data():
    df, _ = load_clean_arrays()
    return df

df = get_data()

# ---------------------------------------------------------------
# Sidebar filters
# ---------------------------------------------------------------
st.sidebar.header("Filters")

regions = ["All"] + sorted(df["Region"].unique().tolist())
categories = ["All"] + sorted(df["Category"].unique().tolist())
cust_types = ["All"] + sorted(df["Customer_Type"].unique().tolist())
payment_modes = ["All"] + sorted(df["Payment_Mode"].unique().tolist())

sel_region = st.sidebar.selectbox("Region", regions)
sel_category = st.sidebar.selectbox("Category", categories)
sel_cust_type = st.sidebar.selectbox("Customer Type", cust_types)
sel_payment = st.sidebar.selectbox("Payment Mode", payment_modes)

filtered = df.copy()
if sel_region != "All":
    filtered = filtered[filtered["Region"] == sel_region]
if sel_category != "All":
    filtered = filtered[filtered["Category"] == sel_category]
if sel_cust_type != "All":
    filtered = filtered[filtered["Customer_Type"] == sel_cust_type]
if sel_payment != "All":
    filtered = filtered[filtered["Payment_Mode"] == sel_payment]

if filtered.empty:
    st.warning("No orders match the selected filters.")
    st.stop()

arrays = to_numpy_arrays(filtered)

# ---------------------------------------------------------------
# KPI cards
# ---------------------------------------------------------------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Sales", f"₹{total_revenue(arrays['sales']):,.0f}")
c2.metric("Total Profit", f"₹{total_profit(arrays['profit']):,.0f}")
c3.metric("Total Orders", f"{order_count(arrays['sales']):,}")
c4.metric("Total Customers", f"{unique_customer_count(arrays['customer_id']):,}")

c5, c6, c7 = st.columns(3)
c5.metric("Total Quantity Sold", f"{total_quantity(arrays['quantity']):,.0f}")
c6.metric("Average Order Value", f"₹{average_order_value(arrays['sales']):,.0f}")
c7.metric("Profit Margin", f"{profit_margin_percent(arrays['sales'], arrays['profit']):.1f}%")

st.divider()

# ---------------------------------------------------------------
# Charts
# ---------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    monthly = monthly_totals(arrays["month"], arrays["sales"])
    st.pyplot(monthly_sales_trend(list(monthly.keys()), list(monthly.values())))

    cat_sales = group_sum(arrays["category"], arrays["sales"])
    labels = list(cat_sales.keys())
    values = list(cat_sales.values())
    st.pyplot(sales_by_category(labels, values))

    region_sales = group_sum(arrays["region"], arrays["sales"])
    st.pyplot(sales_by_region(list(region_sales.keys()), list(region_sales.values())))

with col2:
    cat_profit = group_sum(arrays["category"], arrays["profit"])
    st.pyplot(profit_by_category(list(cat_profit.keys()), list(cat_profit.values())))

    product_sales = group_sum(filtered["Product"].to_numpy(dtype=str), arrays["sales"])
    top_10 = top_n(product_sales, n=10)
    st.pyplot(top_products([p[0] for p in top_10], [p[1] for p in top_10]))

    ctype_orders = filtered["Customer_Type"].value_counts()
    st.pyplot(orders_per_customer_type(ctype_orders.index.tolist(), ctype_orders.values.tolist()))

st.divider()

# ---------------------------------------------------------------
# Top customers table
# ---------------------------------------------------------------
st.subheader("Top 10 Customers by Revenue")
cust_sales = group_sum(arrays["customer_id"], arrays["sales"])
top_customers = top_n(cust_sales, n=10)
st.dataframe(
    pd.DataFrame(top_customers, columns=["Customer_ID", "Total_Sales"]),
    use_container_width=True,
)

st.caption(
    f"Repeat customer rate in current filter: "
    f"{repeat_customer_percentage(arrays['customer_id']):.1f}%"
)
