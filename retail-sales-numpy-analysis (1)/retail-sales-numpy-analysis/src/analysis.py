"""
analysis.py
------------
All business analysis for the Retail Sales project, built with NumPy.

WHY A SEPARATE FILE
Keeping analysis functions here (instead of only in the notebook) means
the Streamlit dashboard and the notebook both call the SAME tested code,
so numbers never disagree between the two. This mirrors how real Data
Analyst teams structure "analysis" logic as reusable functions.

Each function below is intentionally small and named after the business
question it answers.
"""

import numpy as np


# ---------------------------------------------------------------
# BASIC KPIs
# ---------------------------------------------------------------

def total_revenue(sales: np.ndarray) -> float:
    """Total Sales. np.sum() adds every value in the array in one call."""
    return float(np.sum(sales))


def total_profit(profit: np.ndarray) -> float:
    return float(np.sum(profit))


def total_quantity(quantity: np.ndarray) -> float:
    return float(np.sum(quantity))


def unique_customer_count(customer_id: np.ndarray) -> int:
    """np.unique() returns each distinct value once - perfect for counting
    distinct customers without loops."""
    return int(np.unique(customer_id).size)


def order_count(sales: np.ndarray) -> int:
    return int(sales.shape[0])


def average_order_value(sales: np.ndarray) -> float:
    """AOV = Total Sales / Number of Orders."""
    return float(np.mean(sales))


def average_profit_per_order(profit: np.ndarray) -> float:
    return float(np.mean(profit))


def profit_margin_percent(sales: np.ndarray, profit: np.ndarray) -> float:
    """Profit Margin % = Total Profit / Total Sales * 100."""
    return float(np.sum(profit) / np.sum(sales) * 100)


# ---------------------------------------------------------------
# DESCRIPTIVE STATISTICS (EDA)
# ---------------------------------------------------------------

def summary_stats(arr: np.ndarray) -> dict:
    """
    Returns mean, median, min, max, std, and 25th/75th percentile for
    any numeric array (e.g. sales, profit, discount, quantity).

    Why each statistic matters to a Data Analyst:
    - mean: typical order size, but sensitive to outliers (a few huge orders
      can pull it up).
    - median: the "middle" value - a more honest typical value when data
      is skewed (e.g. a handful of very large orders).
    - std (standard deviation): how spread out order values are. High std
      means inconsistent order sizes.
    - percentiles: help identify what a "high" or "low" order looks like,
      useful for setting business thresholds (e.g. "top 25% of orders").
    """
    return {
        "mean": float(np.mean(arr)),
        "median": float(np.median(arr)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
        "std": float(np.std(arr)),
        "p25": float(np.percentile(arr, 25)),
        "p75": float(np.percentile(arr, 75)),
    }


# ---------------------------------------------------------------
# BOOLEAN MASKING / FILTERING
# ---------------------------------------------------------------

def high_value_orders(sales: np.ndarray, threshold: float = 5000) -> np.ndarray:
    """Boolean masking: sales > threshold returns True/False for every
    element; sales[mask] keeps only the True positions."""
    mask = sales > threshold
    return sales[mask]


def profitable_orders_mask(profit: np.ndarray) -> np.ndarray:
    """Returns a boolean array marking which orders were profitable."""
    return profit > 0


def high_discount_orders(discount: np.ndarray, sales: np.ndarray, min_discount: float = 0.15):
    """Combine two conditions with & (both must be True)."""
    mask = (discount >= min_discount) & (sales > 0)
    return sales[mask], discount[mask]


def flag_orders_np_where(profit: np.ndarray) -> np.ndarray:
    """
    np.where(condition, value_if_true, value_if_false) builds a new array
    by choosing between two values for every element - a fast, loop-free
    way to label data.
    """
    return np.where(profit > 0, "Profitable", "Loss")


# ---------------------------------------------------------------
# GROUP-STYLE AGGREGATION (the NumPy equivalent of SQL GROUP BY)
# ---------------------------------------------------------------

def group_sum(group_labels: np.ndarray, values: np.ndarray) -> dict:
    """
    Mimics SQL's `GROUP BY <label> -> SUM(<values>)`.

    SQL:      SELECT Category, SUM(Sales) FROM sales GROUP BY Category;
    NumPy:    for each unique label, build a boolean mask and sum the
              matching values.

    We use np.unique() to find the groups, then boolean masking + np.sum()
    to aggregate each group. This is the conceptual bridge between SQL
    (which does grouping automatically) and NumPy (where we build the
    grouping manually using array operations).
    """
    labels = np.unique(group_labels)
    result = {}
    for label in labels:
        mask = group_labels == label
        result[label] = float(np.sum(values[mask]))
    return result


def top_n(group_totals: dict, n: int = 5, ascending: bool = False) -> list:
    """
    Sort a {label: total} dictionary and return the top N.
    Internally converts to NumPy arrays and uses np.argsort(), which
    returns the INDEX order that would sort the array (not the sorted
    values themselves) - useful when you need to sort one array based
    on another (here: sort labels by their totals).
    """
    labels = np.array(list(group_totals.keys()))
    totals = np.array(list(group_totals.values()))
    order = np.argsort(totals)
    if not ascending:
        order = order[::-1]  # reverse for descending order
    top_labels = labels[order][:n]
    top_totals = totals[order][:n]
    return list(zip(top_labels, top_totals))


# ---------------------------------------------------------------
# CUSTOMER ANALYSIS
# ---------------------------------------------------------------

def repeat_customer_percentage(customer_id: np.ndarray) -> float:
    """
    A "repeat customer" is one who appears more than once in the dataset.
    np.unique(..., return_counts=True) gives both the unique IDs and how
    many times each one appears - exactly what we need here.
    """
    _, counts = np.unique(customer_id, return_counts=True)
    repeat_customers = np.sum(counts > 1)
    return float(repeat_customers / counts.size * 100)


def top_customers_by_revenue(customer_id: np.ndarray, sales: np.ndarray, n: int = 10):
    totals = group_sum(customer_id, sales)
    return top_n(totals, n=n)


# ---------------------------------------------------------------
# TIME ANALYSIS
# ---------------------------------------------------------------

def monthly_totals(month: np.ndarray, values: np.ndarray) -> dict:
    """Group Sales or Profit by Year-Month string, e.g. '2024-03'."""
    totals = group_sum(month, values)
    # sort chronologically (the labels are 'YYYY-MM' strings, which sort correctly as text)
    return dict(sorted(totals.items()))


# ---------------------------------------------------------------
# NUMPY CONCEPT DEMOS (used in the notebook's teaching sections)
# ---------------------------------------------------------------

def demo_array_vs_list():
    """
    Shows why NumPy arrays beat Python lists for numeric work:
    a vectorized operation (array * 2) applies to every element at once,
    while a plain list requires a loop or list comprehension.
    """
    py_list = [10, 20, 30, 40]
    np_array = np.array(py_list)

    # Doubling every value:
    # Python list -> needs a loop / comprehension
    doubled_list = [x * 2 for x in py_list]
    # NumPy array -> broadcasting does it directly, and faster on large data
    doubled_array = np_array * 2

    return doubled_list, doubled_array


def demo_reshape_stack():
    """Small demo of reshape(), vstack(), hstack(), concatenate()."""
    a = np.arange(6)              # [0 1 2 3 4 5]
    reshaped = a.reshape(2, 3)    # 2 rows x 3 cols

    b = np.array([100, 200, 300])
    stacked_v = np.vstack([reshaped, b])       # add b as a new row
    stacked_h = np.hstack([reshaped, reshaped])  # place side-by-side
    combined = np.concatenate([a, b])            # join into one flat array

    return reshaped, stacked_v, stacked_h, combined
