# Interview Preparation — Based on This Project

Each answer is written the way you could actually say it out loud. The
"What interviewer is testing" line tells you what's really being
evaluated, so you can adapt your answer under pressure.

## Python Questions

**1. Why did you use pandas to load the CSV instead of pure NumPy?**
Answer: The dataset mixes text columns (names, categories) with numeric
columns, and has some missing/malformed values. `pandas.read_csv()`
handles that reliably; `np.genfromtxt()` struggles with mixed types. I
converted the numeric columns to NumPy arrays right after loading, since
NumPy is what I used for the actual analysis.
*Tests: whether you understand tool tradeoffs, not just tool names.*

**2. What's the difference between a Python list and a NumPy array?**
Answer: A list can hold anything and needs a loop for math on every
element. A NumPy array is built for numeric data — an operation like
`array * 2` applies to every element at once (vectorization), and it's
much faster on large datasets.
*Tests: fundamental understanding, not memorized definitions.*

**3. How did you handle missing or invalid values in this project?**
Answer: I identified them with `.isna()` checks and value ranges, then
removed rows with missing Quantity/Price/Date and removed negative
quantities, since those are business-impossible values.
*Tests: whether you can justify a cleaning decision, not just perform one.*

## NumPy Questions

**4. Why did you use NumPy for this project instead of just pandas?**
Answer: NumPy is the foundation pandas is built on, and this project was
specifically about practicing NumPy's core operations — vectorization,
Boolean masking, aggregation — which are the same operations pandas uses
internally, just without the wrapper.
*Tests: whether you understand NumPy's role in the data stack.*

**5. What is Boolean masking?**
Answer: Applying a condition like `sales > 5000` to an array returns a
same-length array of True/False values. Indexing the original array with
that Boolean array keeps only the True positions — a fast way to filter
without a loop.
*Tests: core NumPy competency — this comes up constantly.*

**6. Why is vectorization useful?**
Answer: It replaces explicit loops with operations that run across the
whole array at once, which is both faster (NumPy runs in optimized C
code under the hood) and easier to read.
*Tests: whether you understand *why* NumPy is fast, not just that it is.*

**7. Why did you use both mean and median in your analysis?**
Answer: Mean can be skewed by a few very large orders. Comparing mean and
median tells you whether that's happening — if they're far apart, the
data is skewed and median is the more honest "typical" value.
*Tests: statistical judgment, not just knowing the formulas.*

**8. What does `np.where()` do, and where did you use it?**
Answer: It builds a new array by choosing between two values based on a
condition, for every element. I used it to label each order
"Profitable" or "Loss" based on whether Profit was positive.
*Tests: practical, applied NumPy knowledge.*

**9. How does `np.argsort()` differ from `np.sort()`?**
Answer: `np.sort()` returns the values in sorted order. `np.argsort()`
returns the *indices* that would produce that order — useful when you
need to sort one array (like customer totals) based on another (like
customer IDs) together.
*Tests: whether you've actually used both, not just one.*

## Data Analysis Questions

**10. What is the difference between revenue and profit?**
Answer: Revenue (Sales) is the total money received from a sale. Profit
is what's left after subtracting the cost of the product — revenue minus
cost.
*Tests: basic business literacy, expected of any Data Analyst.*

**11. What is Average Order Value (AOV) and why does it matter?**
Answer: AOV is total sales divided by number of orders — the typical
amount a customer spends per transaction. It's a quick health metric:
if it drops, customers are buying less per visit even if order count is
stable.
*Tests: whether you can connect a metric to a business meaning.*

**12. What business insight did you find in this project?**
Answer: Give your actual top category, weakest region, and repeat-
customer percentage from Section 16 of the notebook, and explain *why*
each matters, not just what the number was.
*Tests: whether you can speak to your own findings specifically.*

**13. What's the difference between an observation, an insight, and a
recommendation?**
Answer: An observation is a plain fact ("Electronics had the highest
sales"). An insight adds why it matters ("...suggesting strong demand").
A recommendation is a specific action ("prioritize Electronics
inventory"). Good analysis moves through all three.
*Tests: analytical maturity — a very common interview differentiator.*

**14. How did you connect this project to SQL, which you also learned?**
Answer: I mapped SQL's `GROUP BY` to NumPy's manual grouping approach:
`np.unique()` to find the distinct group labels, then a Boolean mask +
`np.sum()` per group — the same result, built by hand instead of
automatically.
*Tests: whether you can transfer concepts across tools.*

## Business Questions

**15. Who is the target user of your dashboard?**
Answer: A retail manager who wants a quick, filterable view of sales,
profit, and customer performance without needing to write code or SQL
themselves.
*Tests: whether you think about the audience, not just the code.*

**16. If sales are up but profit is flat, what would you investigate?**
Answer: Discount levels and cost — rising discounts or rising costs can
grow revenue while eating profit. I'd check profit margin by category or
month to isolate where it's happening.
*Tests: business reasoning under a hypothetical.*

## Git/GitHub Questions

**17. Why did you use Git/GitHub for this project?**
Answer: Version control tracks every change with history, and GitHub
makes the project visible as a public portfolio piece that recruiters
and interviewers can review directly.
*Tests: whether you understand *why* you use these tools, not just the commands.*

**18. What does `.gitignore` do, and why did you use one?**
Answer: It tells Git which files to never track — like cached Python
bytecode (`__pycache__/`) or local environment folders (`venv/`) — so
the repository stays clean and doesn't include machine-specific or
temporary files.
*Tests: attention to repository hygiene, a real signal of experience.*

## Project Questions

**19. Why did you deploy the project instead of just sharing the code?**
Answer: A deployed dashboard lets anyone — including a non-technical
interviewer — interact with the analysis directly, which demonstrates
the work more convincingly than a static script.
*Tests: whether you understand the value of a finished, usable product.*

**20. How would you improve this project further?**
Answer: Point to the "Future Improvements" section of the README — for
example, adding year-over-year comparisons or customer segmentation —
and explain why that's a logical next step given the current analysis.
*Tests: whether you can think beyond "done," a sign of growth mindset.*
