"""
data_loader.py
---------------
Loads the retail sales CSV and cleans it.

WHY THIS FILE EXISTS
Every analysis step depends on clean, correctly-typed data.
Instead of repeating cleaning code in the notebook AND the
Streamlit app, we write it once here and import it in both places.
This is a common real-world Data Analyst practice: keep your
cleaning logic in one place so results stay consistent everywhere.

We use pandas ONLY to read the CSV conveniently (mixed text +
numeric columns are painful with plain NumPy). Immediately after
loading, we convert the numeric columns we analyze into NumPy
arrays, because NumPy is the tool we use for the actual analysis.
"""

import numpy as np
import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "retail_sales.csv")


def load_raw_data(path: str = DATA_PATH) -> pd.DataFrame:
    """Load the CSV exactly as-is, with no cleaning applied yet."""
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the raw dataset.

    Steps (in order):
    1. Strip extra whitespace from text columns.
    2. Standardize Category text (fix "electronics" vs "Electronics" vs " Electronics ").
    3. Remove rows with missing Quantity, Unit_Price, or Order_Date.
    4. Remove rows with negative or zero Quantity.
    5. Remove duplicate Order_IDs (keep the first occurrence).
    6. Recompute Sales, Cost, Profit as numeric columns (defensive - in case
       any slipped through as text/blank).
    7. Parse Order_Date into a real datetime column; drop unparseable dates.

    Each step is explained because a beginner Data Analyst must be able to
    justify every cleaning decision, not just run code that "works".
    """
    df = df.copy()

    # 1. Strip whitespace from all text (object) columns
    text_cols = df.select_dtypes(include="object").columns
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()

    # 2. Standardize category text: lowercase -> title case, fix "and" vs "&"
    df["Category"] = (
        df["Category"]
        .str.replace(" and ", " & ", case=False, regex=False)
        .str.title()
        .str.replace("&", "&")
    )

    # 3. Drop rows where core numeric fields are missing (blank strings after strip)
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")
    df = df.dropna(subset=["Quantity", "Unit_Price"])

    # 4. Remove invalid (negative or zero) quantity - a sale of 0 or -2 items
    #    makes no business sense and would distort every downstream total.
    df = df[df["Quantity"] > 0]

    # 5. Remove duplicate Order_IDs - each order should appear once.
    df = df.drop_duplicates(subset="Order_ID", keep="first")

    # 6. Recompute financial columns from source values so they are always
    #    consistent with cleaned Quantity/Unit_Price/Discount.
    df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce").fillna(0)
    df["Sales"] = (df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])).round(2)
    # Cost wasn't independently reliable as text; recompute using original
    # Cost column when present and numeric, otherwise estimate at 70% of sales.
    df["Cost"] = pd.to_numeric(df["Cost"], errors="coerce")
    df["Cost"] = df["Cost"].fillna(df["Sales"] * 0.7).round(2)
    df["Profit"] = (df["Sales"] - df["Cost"]).round(2)

    # 7. Parse dates; drop rows where the date could not be understood.
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    df = df.dropna(subset=["Order_Date"])

    df = df.reset_index(drop=True)
    return df


def to_numpy_arrays(df: pd.DataFrame) -> dict:
    """
    Convert the key numeric columns of the cleaned DataFrame into a
    dictionary of NumPy arrays. This is the hand-off point where we move
    from "table" thinking (pandas) to "array" thinking (NumPy), which is
    the core skill this project is built to teach.
    """
    arrays = {
        "quantity": df["Quantity"].to_numpy(dtype=np.float64),
        "unit_price": df["Unit_Price"].to_numpy(dtype=np.float64),
        "discount": df["Discount"].to_numpy(dtype=np.float64),
        "sales": df["Sales"].to_numpy(dtype=np.float64),
        "cost": df["Cost"].to_numpy(dtype=np.float64),
        "profit": df["Profit"].to_numpy(dtype=np.float64),
        "category": df["Category"].to_numpy(dtype=str),
        "city": df["City"].to_numpy(dtype=str),
        "region": df["Region"].to_numpy(dtype=str),
        "customer_id": df["Customer_ID"].to_numpy(dtype=str),
        "payment_mode": df["Payment_Mode"].to_numpy(dtype=str),
        "customer_type": df["Customer_Type"].to_numpy(dtype=str),
        "order_date": df["Order_Date"].to_numpy(),
        "month": df["Order_Date"].dt.to_period("M").astype(str).to_numpy(dtype=str),
    }
    return arrays


def load_clean_arrays(path: str = DATA_PATH):
    """Convenience function: load -> clean -> return (DataFrame, arrays dict)."""
    raw = load_raw_data(path)
    clean = clean_data(raw)
    arrays = to_numpy_arrays(clean)
    return clean, arrays


if __name__ == "__main__":
    raw_df = load_raw_data()
    print(f"Raw rows: {len(raw_df)}")
    clean_df, arr = to_numpy_arrays(clean_data(raw_df)), None
    clean_df = clean_data(raw_df)
    print(f"Clean rows: {len(clean_df)}  (removed {len(raw_df) - len(clean_df)})")
