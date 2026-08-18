# Student Challenge — Independent Practice

Complete these on your own, using the cleaned data and the functions in
`src/analysis.py` as a starting point. Hints are provided — full
solutions are not, so you build the skill yourself.

1. **Find the product with the highest profit margin** (not just highest
   profit). *Hint: profit margin = profit / sales × 100 per product,
   which needs profit and sales grouped by Product, then divided.*

2. **Find the top 5 cities by revenue.** *Hint: reuse `group_sum()` and
   `top_n()` from `src/analysis.py`, but group by City instead of Category.*

3. **Find customers whose revenue is above the average customer's
   revenue.** *Hint: compute `group_sum()` by customer, then filter that
   result using a Boolean condition against `np.mean()` of the totals.*

4. **Find the month with the highest profit** without using `max()` on a
   dict — do it with `np.argsort()` on a NumPy array of monthly totals
   instead. *Hint: convert `monthly_totals()`'s values into an array
   first.*

5. **Find products with high sales but low profit margin** — these are
   often prime candidates for a pricing review. *Hint: you'll need both
   Sales and Profit grouped by Product, then compare margin per product
   against a threshold, e.g. below 20%.*

6. **Find the category with the highest average order value.** *Hint:
   this isn't the same as highest total sales — you need Sales divided
   by order count, per category.*

7. **Find what percentage of total revenue comes from the top 10%
   highest-value orders.** *Hint: use `np.percentile()` to find the
   90th-percentile sales value, then sum everything above it.*

8. **Find which payment mode is associated with the highest average
   order value.**

9. **Find the region with the best profit margin** (not just highest
   total profit).

10. **Add a new calculated column: Profit_Per_Unit** (Profit ÷
    Quantity), then find the product with the highest Profit_Per_Unit.

## Rules
- Don't hardcode values you could calculate — every answer should come
  from actual NumPy operations on the dataset.
- Write your work as new functions in a copy of `src/analysis.py`, or in
  a new notebook cell — either is fine.
- Try to answer using NumPy directly before falling back on pandas
  shortcuts; the practice value is in the NumPy operations.
