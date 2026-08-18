# Troubleshooting — Common Beginner Errors

| Error | Why it happens | Solution |
|---|---|---|
| `ModuleNotFoundError: No module named 'numpy'` (or pandas/streamlit) | The package isn't installed in your active environment | Run `pip install -r requirements.txt`. If using a virtual environment, make sure it's activated first. |
| `FileNotFoundError: retail_sales.csv` | The script is being run from the wrong folder, so the relative path doesn't resolve | Run commands from the project root, or check the path used in `data_loader.py` (`DATA_PATH`) matches where the CSV actually is. |
| CSV path problem when deploying | Community Cloud runs your app from the repo root — a path that worked locally may not exist there | Use paths relative to the project root (as `data_loader.py` already does with `os.path.dirname(__file__)`), and confirm `data/retail_sales.csv` was actually committed and pushed to GitHub. |
| NumPy array shape mismatch (e.g. `ValueError: operands could not be broadcast together`) | Two arrays you're combining have different lengths — often because one was filtered and the other wasn't | Make sure any Boolean mask is applied to *all* arrays you're comparing, using the exact same mask. |
| Invalid data type (`could not convert string to float`) | A column has an unexpected value (blank, text, or symbol) where a number is expected | Use `pd.to_numeric(column, errors="coerce")` to convert safely, turning bad values into `NaN` you can then drop or fix. |
| Streamlit application not starting locally | Wrong command, wrong folder, or Streamlit not installed | Run `streamlit run app.py` from the project root with your virtual environment activated. |
| `requirements.txt` problem on deploy (build fails) | A typo in a package name, or a version pin that doesn't exist | Check spelling of each package name; remove version pins unless you have a specific reason to keep them. |
| `git push` rejected (`! [rejected] main -> main`) | The remote repository has commits your local copy doesn't have | Run `git pull origin main --rebase`, resolve any conflicts, then push again. |
| GitHub repository connection issue in Streamlit Community Cloud | Streamlit hasn't been granted access to the repository, or the repo is private without proper authorization | In Community Cloud settings, reconnect your GitHub account and confirm repository access permissions. |
