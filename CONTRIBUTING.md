# 🤝 Contributing to the Brazilian Financial Markets Toolkit

Thank you for your interest in contributing! We appreciate your help in making this project better. This guide outlines the process for making a successful contribution.

## ⚙️ Getting Started

### 1. Prerequisites
Ensure you have the following installed:
* **Git**
* **Docker** and **Docker Compose** (Highly Recommended for a consistent environment)
* **Python 3.8+** and **Node.js 16+** (If you prefer not to use Docker)

### 2. Setup the Development Environment
We use **Docker** for local development to ensure environment consistency.

1.  **Fork the Repository:** Click the 'Fork' button on the main repository page.
2.  **Clone Your Fork:**
    ```bash
    git clone [https://github.com/bratergit/brazilstocks.git](https://github.com/bratergit/brazilstocksstocks.git)
    cd stocks
    ```
3.  **Build and Run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    This command will build the necessary Python and Node.js service images and start the containers.

## 🔄 The Pull Request (PR) Workflow

Follow these steps to ensure your contribution can be reviewed and merged efficiently:

### Step 1: Create a New Branch
Always work in a new, descriptive branch. Use prefixes like `feat/`, `fix/`, or `docs/`.

```bash
# Example: Creating a new feature branch
git checkout -b feat/add-b3-screener
```

Step 2: Make Your Changes
Implement your feature, fix the bug, or update the documentation. Ensure your code follows the existing style and conventions.

Step 3: Commit Your Changes
Write clear and concise commit messages. Follow the Conventional Commits specification (e.g., feat: add new B3 stock screener).

Bash

git add .
git commit -m "feat: implement basic SELIC rate calculation function"
Step 4: Push to Your Fork
Upload your changes to your fork on GitHub.

Bash

git push origin feat/add-b3-screener
Step 5: Open a Pull Request (PR)
Go to your fork on GitHub and click the 'Compare & pull request' button.

Fill out the PR Template: Provide a detailed description of your changes.

Reference the Issue: Link your PR to the relevant issue using keywords like Closes #XX or Fixes #YY.

Describe the Solution: Explain what you did and why.

Screenshots/Demos: Include visual aids for UI changes (e.g., Streamlit dashboards).

Submit your PR. A maintainer will review it, provide feedback, and merge it upon approval.


