# 🏆 Inter Class Coding League (ICL) - Python Debugging Competition
**Organized by ENCIDE**

Welcome to the **Python Debugging Competition**, a part of the **Inter Class Coding League (ICL)** organized by **ENCIDE MACE**! This competition is designed to test your problem-solving skills, understanding of Python, and debugging abilities. 

You will find **10 Python files** in the `problems/` directory. Each file contains a function designed to solve a specific programming problem. However, **every single solution has both syntax errors (which prevent the code from running) and logical errors (which produce incorrect results).**

Your task is to find and fix all these errors so that the code runs correctly and passes all the test cases!

---

## 🚀 Step-by-Step Guide

### Step 1: Fork the Repository
1. Open this repository on GitHub.
2. Click the **Fork** button in the top-right corner of the page. This creates a personal copy of the repository under your own GitHub account.

### Step 2: Clone the Repository
Clone **your forked repository** to your local computer:
1. Click the green **Code** button on your forked GitHub repository page and copy the URL.
2. Open your terminal (or Command Prompt / PowerShell) and run:
   ```bash
   git clone <YOUR_FORKED_REPOSITORY_URL>
   ```
3. Navigate into the project directory:
   ```bash
   cd DebugCompetition
   ```

### Step 3: Set Up Your Python Environment
Ensure you have Python 3 installed. You can check by running:
```bash
python --version
```
*(On macOS/Linux, you might need to use `python3`).*

We recommend using a virtual environment (optional but recommended):
```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate it (Windows Command Prompt)
.\venv\Scripts\activate.bat

# Activate it (macOS/Linux)
source venv/bin/activate
```

### Step 4: Testing Your Solutions
We have provided two testing scripts in the root of the repository to check your work:

* **Run all tests at once**:
  ```bash
  python run_tests.py
  ```
* **Run a specific test individually** (e.g., Problem 3):
  ```bash
  python run_test.py 3
  ```
* **Run a specific test (Interactive Mode)**: If you run `run_test.py` without arguments, it will ask you for a problem number:
  ```bash
  python run_test.py
  ```

These scripts run the `unittest` suites located in the `tests/` directory.

---

## 🛠 How the Competition Works

There are 10 files inside the `problems/` directory (e.g., `problem_1.py`, `problem_2.py`, etc.).

1. **Read the docstring**: Each file contains a detailed description of the problem, input formats, output formats, and example test cases inside the docstring at the top of the file.
2. **Fix Syntax Errors**: First, correct any syntax errors (like missing colons, invalid indentation, typos in keywords) so the Python file is executable.
3. **Fix Logical Errors**: Next, correct any logical bugs in the code (like off-by-one errors, incorrect operators, wrong returns) to make sure the function behaves exactly as specified.
4. **Do NOT change the function names or arguments!** The automated tests rely on these names to grade your submissions.

---

## 📤 Submitting Your Work

Once you have fixed the bugs and are satisfied with your solutions, submit your work back to GitHub:

1. **Check which files you modified**:
   ```bash
   git status
   ```
2. **Stage your changes**:
   ```bash
   git add .
   ```
3. **Commit your changes** with a meaningful message:
   ```bash
   git commit -m "Solved problems 1 to 10"
   ```
4. **Push your changes** to your forked repository on GitHub:
   ```bash
   git push origin main
   ```
5. **Create a Pull Request to Submit Your Entry**:
   Once your code is pushed to your GitHub fork, you need to submit it to the organizers by creating a Pull Request (PR) from your fork back to the main repository. 
   
   If you need help with this step, [click here for tutorial](https://www.youtube.com/watch?v=XBIVUwmMcwc) showing how to submit from a fork.
   
   **Step-by-step instructions**:
   * Navigate to **your forked repository** on GitHub.
   * Right above the file list, click the **"Contribute"** dropdown button and select **"Open pull request"**.
   * On the comparison page, ensure that:
     * **base repository** is the original competition repository (`main` branch).
     * **head repository** is your forked repository (`main` branch).
    * ⚠️ **Crucial Step**: Set the title of your Pull Request to **your own full name** (e.g., "John Doe") so the organizers can track and grade your submission!
    * Click the final green **"Create pull request"** button to submit.
   
   Once your Pull Request is opened, a **GitHub Action** will automatically run and benchmark your solutions to calculate their average execution times. You will be able to see these timing results directly in the action logs!

---

## 💡 Tips for Success
- **Read the error messages**: Python's tracebacks tell you exactly where the syntax error is or what line caused a crash.
- **Dry run with simple inputs**: If you get a logical error, trace the code line by line with a small example on paper.
- **Edge cases matter**: Pay close attention to empty lists, negative numbers, extreme values, or single-character inputs.
- **Write print statements**: You can temporarily add `print()` statements inside the functions to see what values variables hold as the code runs.

---

## 📺 Git & GitHub Tutorial for Beginners

If you are new to Git and GitHub, don't worry! Here is a highly recommended, beginner-friendly video tutorial to get you up to speed:

* **[Git & GitHub Crash Course - YouTube](https://www.youtube.com/watch?v=a9u2yZvsqHA)**

Good luck, and happy debugging! 🐍
