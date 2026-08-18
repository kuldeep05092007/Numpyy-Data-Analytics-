# Project Evaluation Rubric (100 Marks)

| Area | Marks | What Qualifies for Full Marks |
|---|---|---|
| Dataset Understanding | 10 | Student can explain every column's meaning and business purpose without referring to notes. |
| Data Cleaning | 10 | All specified issues (missing values, duplicates, invalid values, inconsistent text) are identified, fixed, and verified with before/after counts. |
| NumPy Usage | 20 | Uses at least 10 distinct NumPy operations meaningfully (not decoratively), including Boolean masking, `np.where()`, aggregation, and at least one statistics function, each tied to a real business question. |
| Data Analysis | 15 | Answers at least 15 of the 20+ business questions correctly, with the correct NumPy/aggregation approach. |
| Visualization | 10 | At least 6 charts, each with a title, axis labels, and a written explanation of what business question it answers. |
| Business Insights | 10 | At least 10 insights, each clearly distinguishing observation vs. insight vs. recommendation, and grounded in actual calculated numbers (no invented claims). |
| Streamlit Dashboard | 10 | Dashboard runs locally without errors, displays all required KPIs, and includes working filters for Region, Category, Customer Type, and Payment Mode. |
| GitHub Repository | 5 | Repository is public, properly structured, includes `.gitignore`, and has a clean commit history (not one giant commit with no message). |
| README | 5 | Includes all required sections, uses professional (non-promotional) language, and accurately reflects the actual project. |
| Project Presentation | 5 | Delivered within 5–7 minutes, covers all 12 structure points, and answers follow-up questions accurately. |
| **Total** | **100** | |

## Grading Notes for Trainers
- Deduct marks for invented or unsupported "insights" — this is a core
  professional skill being assessed, not just a formatting nicety.
- Deduct marks if NumPy operations could be replaced by a single pandas
  one-liner with no NumPy involved at all — the objective is NumPy
  fluency, not just a working result.
- A dashboard that runs locally but was never deployed should not lose
  more than the 10 dashboard marks — deployment issues are common and
  shouldn't overly penalize otherwise solid analysis work.
