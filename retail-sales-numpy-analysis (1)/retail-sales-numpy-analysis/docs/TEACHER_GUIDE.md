# Teacher Guide — Teaching This Project in 7 Classes

Prerequisite: students have completed Excel, SQL, Python basics, and NumPy.

## Class 1 — Project Introduction + Dataset + Business Problem
- **Objectives:** Understand the business scenario and dataset structure.
- **Topics:** Project overview, business questions, dataset columns.
- **Live coding:** Load the CSV with pandas, run `.info()`, `.head()`, `.isna().sum()`.
- **Student practice:** List 5 business questions they'd want answered from this data.
- **Homework:** Read README.md fully; sketch (on paper) what KPIs they expect to be highest.
- **Expected outcome:** Students can explain the business problem in their own words.

## Class 2 — Data Loading + Cleaning + NumPy Arrays
- **Objectives:** Understand why cleaning matters and how to convert to NumPy arrays.
- **Topics:** Missing values, duplicates, invalid values, `to_numpy_arrays()`.
- **Live coding:** Walk through `src/data_loader.py -> clean_data()` line by line.
- **Student practice:** Deliberately break a cleaning rule (e.g. comment out the duplicate-removal step) and observe how row counts and KPIs change.
- **Homework:** Write a one-paragraph explanation of why each cleaning step is necessary.
- **Expected outcome:** Students can justify every cleaning decision, not just copy the code.

## Class 3 — NumPy Calculations + Statistics + Filtering
- **Objectives:** Practice core NumPy operations on real data.
- **Topics:** `np.mean`, `np.median`, `np.std`, `np.percentile`, Boolean masking, `np.where`.
- **Live coding:** Section 8–10 of the notebook.
- **Student practice:** Change the high-value-order threshold from 5000 to a value they choose and interpret the new result.
- **Homework:** Complete Student Challenge questions 1–3.
- **Expected outcome:** Students can write their own Boolean mask from scratch.

## Class 4 — Business Analysis + KPIs
- **Objectives:** Connect NumPy output to business meaning.
- **Topics:** Group-style aggregation, SQL vs. NumPy grouping, top-N ranking.
- **Live coding:** Sections 11–14 of the notebook (product, customer, region, time analysis).
- **Student practice:** Calculate top 5 cities themselves before revealing the answer.
- **Homework:** Complete Student Challenge questions 4–6.
- **Expected outcome:** Students can explain the SQL-`GROUP BY`-to-NumPy mapping unprompted.

## Class 5 — Visualization + Insights
- **Objectives:** Turn numbers into charts and written insights.
- **Topics:** Matplotlib chart types, observation vs. insight vs. recommendation.
- **Live coding:** Section 15–16 of the notebook.
- **Student practice:** Write 3 original insights (not the ones in the notebook) from their own dataset run.
- **Homework:** Draft their 5 business recommendations.
- **Expected outcome:** Students can distinguish an observation from a genuine insight.

## Class 6 — Streamlit Dashboard
- **Objectives:** Turn analysis into an interactive app.
- **Topics:** `st.metric`, `st.pyplot`, sidebar filters, `@st.cache_data`.
- **Live coding:** Walk through `app.py` top to bottom; run it locally.
- **Student practice:** Add one new filter or metric card of their choice.
- **Homework:** Take a screenshot of their working dashboard.
- **Expected outcome:** Students can run the dashboard locally and explain each section of `app.py`.

## Class 7 — GitHub + Deployment + Presentation
- **Objectives:** Publish and present the finished project.
- **Topics:** `git init/add/commit/push`, Streamlit Community Cloud deployment, presentation structure.
- **Live coding:** Full GitHub push (`docs/GITHUB_GUIDE.md`) and deployment (`docs/DEPLOYMENT_GUIDE.md`) walkthrough.
- **Student practice:** Each student pushes their own repo and deploys their own dashboard.
- **Homework:** Prepare a 5–7 minute presentation using `docs/PRESENTATION_GUIDE.md`.
- **Expected outcome:** Every student has a live, public dashboard URL and GitHub repository to add to their resume.
