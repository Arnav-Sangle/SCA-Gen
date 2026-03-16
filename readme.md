# Git Commands Cheatsheet

A quick reference of Git commands commonly used for staging, unstaging, and committing files.

---

## 1. Remove a File or Directory From Git Tracking (Keep Locally)

```bash
git rm -r --cached <file_or_directory>
```

**Explanation**

* `git rm` → Removes a file from Git tracking
* `-r` → Recursive removal (needed for directories)
* `--cached` → Removes from the Git **index only**, keeps the file locally

Example:

```bash
git rm -r --cached __pycache__
```

Used when a file or directory should be ignored by Git but already exists in the repository.

---

## 2. Restore a File to the Staging Area (Undo Unstage)

If you removed a file from staging but haven't committed yet:

```bash
git restore --staged .gitignore
```

**Explanation**

* Moves the file **back into the staging area**
* Useful when you accidentally unstaged something.

---

## 3. Stage Specific Files

Add only selected files to the staging area:

```bash
git add .gitignore sca_recommendations.xlsx
```

**Explanation**

* Adds only the specified files
* Other modified files remain uncommitted

---

## 4. Check What Will Be Committed

```bash
git diff --cached
```

**Explanation**

* Shows the **difference between staged files and the last commit**
* Helps verify changes before committing

---

## 5. Unstage a File

If a file was staged accidentally:

```bash
git restore --staged services/vulnerability_lookup.py
```

**Explanation**

* Removes the file from the staging area
* Keeps the file and changes locally

---

## Quick Workflow Example

```bash
git add .gitignore sca_recommendations.xlsx
git diff --cached
git commit -m "Update gitignore and add SCA recommendations"
```

---

## Helpful Tip

Use `.gitignore` to prevent unwanted files from being tracked, such as:

```
.env
__pycache__/
*.pyc
```

This keeps sensitive files and temporary files out of your repository.

---
