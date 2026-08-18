"""
visualization.py
------------------
Chart functions for the Retail Sales project.

Each function returns a matplotlib Figure so it can be shown in the
notebook (fig.show() / plt.show()) or embedded directly in Streamlit
(st.pyplot(fig)) without duplicating plotting code in two places.

Every chart answers a specific business question - we don't chart data
just to decorate the notebook.
"""

import matplotlib.pyplot as plt
import numpy as np


def _bar_chart(labels, values, title, xlabel, ylabel, horizontal=False, color="#2E86AB"):
    fig, ax = plt.subplots(figsize=(9, 5))
    if horizontal:
        ax.barh(labels, values, color=color)
        ax.invert_yaxis()
    else:
        ax.bar(labels, values, color=color)
        plt.xticks(rotation=45, ha="right")
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.tight_layout()
    return fig


def monthly_sales_trend(months, totals):
    """Line chart: is revenue growing, shrinking, or seasonal month to month?"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(months, totals, marker="o", color="#2E86AB")
    ax.set_title("Monthly Sales Trend", fontsize=13, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Sales (₹)")
    plt.xticks(rotation=60, ha="right")
    fig.tight_layout()
    return fig


def sales_by_category(labels, values):
    """Which product categories bring in the most revenue?"""
    return _bar_chart(labels, values, "Sales by Category", "Category", "Total Sales (₹)")


def profit_by_category(labels, values):
    """Which categories are most profitable (not just highest revenue)?"""
    return _bar_chart(labels, values, "Profit by Category", "Category", "Total Profit (₹)",
                       color="#3E8914")


def top_products(labels, values, n=10):
    """Which individual products sell the most - useful for inventory planning."""
    return _bar_chart(labels[:n], values[:n], f"Top {n} Products by Sales",
                       "Total Sales (₹)", "Product", horizontal=True, color="#F18F01")


def sales_by_region(labels, values):
    """Which regions generate the most revenue - guides regional strategy."""
    return _bar_chart(labels, values, "Sales by Region", "Region", "Total Sales (₹)",
                       color="#A23B72")


def orders_per_customer_type(labels, values):
    """New vs. Returning customer split - measures customer loyalty/retention."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(values, labels=labels, autopct="%1.1f%%",
           colors=["#2E86AB", "#F18F01"], startangle=90)
    ax.set_title("Orders by Customer Type", fontsize=13, fontweight="bold")
    fig.tight_layout()
    return fig
