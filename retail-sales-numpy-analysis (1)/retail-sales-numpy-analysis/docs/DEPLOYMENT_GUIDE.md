# Deployment Guide — Streamlit Community Cloud

This guide deploys `app.py` as a free, public web app using Streamlit
Community Cloud. Steps confirmed current as of August 2026.

## Local Application vs. Deployed Application

- **Local application**: runs only on your computer (`streamlit run app.py`),
  visible only to you at `http://localhost:8501`.
- **Deployed application**: runs on Streamlit's servers with a public URL
  (`https://your-app-name.streamlit.app`) that anyone can open — this is
  what you link from your resume or GitHub profile.

## Steps

1. **Create a GitHub repository** and push this project (see
   `docs/GITHUB_GUIDE.md`). Community Cloud deploys directly from GitHub,
   so the repo must be pushed first.

2. **Push the project** — make sure `app.py`, `requirements.txt`, `src/`,
   and `data/retail_sales.csv` are all committed and pushed to `main`.

3. **Sign in to Streamlit Community Cloud** at
   [share.streamlit.io](https://share.streamlit.io) using your GitHub
   account.

4. **Connect GitHub** — the first time you sign in, Streamlit will ask to
   authorize access to your GitHub repositories.

5. **Create a new app** — from your workspace, click **"Create app"** in
   the upper-right corner, then choose **"Yup, I have an app"**.

6. **Select the repository and branch** — pick
   `<your-username>/retail-sales-numpy-analysis` and branch `main`.

7. **Select the main file path** — enter `app.py`.

8. **Choose an app URL** (optional) — pick a subdomain, e.g.
   `retail-sales-analytics.streamlit.app`.

9. **Deploy** — click **"Deploy"**. Streamlit installs everything in
   `requirements.txt` and starts the app. Most apps go live within a few
   minutes; watch the log output while it builds.

10. **Verify the application** — open the deployed URL and confirm the
    KPI cards, charts, and filters all work exactly as they do locally.

## Things to Know About the Free Tier

- Roughly 1 GB memory per app.
- A public app sleeps after about 12 hours with no traffic (it wakes up
  automatically the next time someone visits).
- One free private app; public apps are unlimited.
- Future pushes to `main` on GitHub redeploy the app automatically —
  you don't need to repeat these steps for every code update.

## Troubleshooting a Failed Deploy

See `docs/TROUBLESHOOTING.md` for the most common deployment errors
(missing dependency, wrong file path, CSV not found) and how to fix each.
