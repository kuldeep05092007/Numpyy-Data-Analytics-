# GitHub Guide

A complete, beginner-friendly walkthrough for putting this project on GitHub.

## Step 1 — Create a GitHub account
Go to github.com and sign up if you don't already have an account.

## Step 2 — Create a repository
On GitHub, click **New repository**.
- **Repository name:** `retail-sales-numpy-analysis`
- **Visibility:** Public (so it's visible on your portfolio)
- **README:** Leave "Add a README" unchecked — this project already has one.

## Step 3 — Create the local project folder
This project folder is already structured correctly. Open a terminal
inside it (the folder containing `README.md`, `app.py`, etc.).

## Step 4 — Initialize Git
```bash
git init
```
This turns the folder into a Git repository, so Git can start tracking changes.

## Step 5 — Add files
```bash
git add .
```
This stages every file in the folder (except anything listed in
`.gitignore`) to be included in the next commit.

## Step 6 — Commit
```bash
git commit -m "Initial project: Retail Sales & Customer Analytics"
```
A commit is a saved snapshot of your project at this point in time, with
a message describing what changed.

## Step 7 — Connect the remote repository
Copy the URL of the GitHub repository you created in Step 2, then run:
```bash
git remote add origin https://github.com/<your-username>/retail-sales-numpy-analysis.git
```
This tells your local Git repository where the online (remote) copy lives.

## Step 8 — Push the project
```bash
git branch -M main
git push -u origin main
```
This uploads your commit to GitHub. `-u` sets `origin main` as the
default target, so future pushes just need `git push`.

## Key Concepts Explained

| Term | Meaning |
|---|---|
| Repository | A project folder tracked by Git, with full history |
| Public repository | Anyone can view it — good for a portfolio |
| README | The first file visitors see; explains the project |
| .gitignore | Tells Git which files/folders to never track |
| Commit | A saved snapshot with a message |
| Push | Uploading your local commits to GitHub |
| Branch | A parallel line of development (`main` is the default) |

## Making future updates

```bash
git add .
git commit -m "Describe what you changed"
git push
```
