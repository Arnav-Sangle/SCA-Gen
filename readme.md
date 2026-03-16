# Git Commands Cheatsheet

A quick reference of Git commands commonly used for staging, unstaging, committing files, checking configuration, and safely using GitHub on shared computers.

---

# 1. Check Git Configuration

```bash
git config --list
```

**Explanation**

* Displays all Git configuration settings currently applied
* Useful for verifying Git identity, credential helpers, and repository configuration

---

# 2. Remove a File or Directory From Git Tracking (Keep Locally)

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

# 3. Restore a File to the Staging Area (Undo Unstage)

```bash
git restore --staged .gitignore
```

**Explanation**

* Moves the file **back into the staging area**
* Useful when you accidentally unstaged something

---

# 4. Stage Specific Files

```bash
git add .gitignore sca_recommendations.xlsx
```

**Explanation**

* Adds only the specified files
* Other modified files remain uncommitted

---

# 5. Check What Will Be Committed

```bash
git diff --cached
```

**Explanation**

* Shows the **difference between staged files and the last commit**
* Helps verify changes before committing

---

# 6. Unstage a File

```bash
git restore --staged services/vulnerability_lookup.py
```

**Explanation**

* Removes the file from the staging area
* Keeps the file and changes locally

---

# Commit Title and Description from Command Line

You can add both a **commit title** and **description** directly from the terminal.

```bash
git commit -m "Add SCA recommendations file" \
           -m "Added sca_recommendations.xlsx containing vulnerability remediation mappings."
```

**Explanation**

* First `-m` → Commit **title**
* Second `-m` → Commit **description**

---

# Quick Workflow Example

```bash
git add .gitignore sca_recommendations.xlsx
git diff --cached
git commit -m "Update gitignore and add SCA recommendations"
```

---

# Change Default Git Commit Editor

Git may open **Vim** when writing commit messages. You can switch to **Notepad**.

```bash
git config --global core.editor "notepad"
```

After this, running:

```bash
git commit
```

will open **Notepad** instead of Vim.

---

# Helpful `.gitignore` Example

```
.env
__pycache__/
*.pyc
```

Used to prevent sensitive files and temporary files from being committed.

---

# Portable GitHub Workflow (Public / Shared Computer)

Use this workflow when working on a **shared or public computer** to avoid saving credentials or identity.

---

## 1. Create a Temporary Workspace

```bash
mkdir temp-work
cd temp-work
```

---

## 2. Clone the Repository

```bash
git clone https://github.com/<username>/<repository>.git
cd <repository>
```

---

## 3. Configure Temporary Git Identity

```bash
git config user.name "Your Name"
git config user.email "your_email@example.com"
```

* Identity is stored **only inside `.git/config`**
* No global Git configuration is saved

---

## 4. Disable Credential Storage

```bash
git config credential.helper ""
```

* Prevents Git from storing credentials locally

---

## 5. Work Normally

```bash
git add .
git commit -m "your commit message"
git push
```

When prompted:

* **Username:** your GitHub username
* **Password:** GitHub Personal Access Token (PAT)

---

## 6. Clean Up After Finishing

```bash
cd ..
rm -rf temp-work
```

Removes:

* repository files
* temporary Git configuration
* commit history

---

## Optional Credential Cleanup

```bash
git credential-manager erase
```

---

# Portable Workflow Summary

* No global Git configuration
* No stored credentials
* Temporary identity only
* Workspace deleted after use
* Leaves minimal traces on shared computers

---
