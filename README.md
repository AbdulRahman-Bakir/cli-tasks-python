# CLI Backend Projects

A collection of backend practice projects built as command-line (CLI) applications in Python.  
Each project is isolated in its own folder and includes setup scripts for easy initialization.

---

## 📁 Projects Overview

| Project # | Project Name              | Description                                            | Dependencies      |
|-----------|---------------------------|--------------------------------------------------------|-------------------|
| 1         | Task Tracker CLI          | Add, update, delete, and list tasks with status management | None (Python stdlib) |
| 2         | Expense Tracker CLI       | Track daily expenses with categories, budgets, and CSV export | colorama, tabulate |
| 3         | GitHub Activity Fetcher   | Fetch and display GitHub user activity events with caching | requests, python-dotenv |
| 4         | Number Guessing Game      | Interactive CLI number guessing game with difficulty levels | None (Python stdlib) |
| 5         | GitHub Trending CLI       | Fetch and display trending GitHub repositories by time range | requests, tabulate |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Git (for cloning the repository)

### General Setup

Each project folder contains its own setup scripts. You can either use the provided scripts or manually set up the virtual environment.

---

## 📋 Project Details & Usage

### 1. Task Tracker CLI

A simple task management system that allows you to add, update, delete, and list tasks with status tracking.

> 📌 Based on the [Task Tracker](https://roadmap.sh/projects/task-tracker) project from [roadmap.sh](https://roadmap.sh).

**Location:** `Task_tracker/`

**Setup:**
```bash
# Navigate to the project folder
cd Task_tracker

# No virtual environment required, but recommended
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

**Usage:**
```bash
# Add a new task
python task_tracker.py add "Complete project documentation"

# Update a task
python task_tracker.py update <task_id> "Updated description"

# Mark task as in-progress
python task_tracker.py mark-in-progress <task_id>

# Mark task as done
python task_tracker.py mark-done <task_id>

# List all tasks
python task_tracker.py list

# List tasks by status
python task_tracker.py list todo
python task_tracker.py list in-progress
python task_tracker.py list done

# Delete a task
python task_tracker.py delete <task_id>
```

**Data Storage:** Tasks are stored in `tasks.json` in the project folder.

---

### 2. Expense Tracker CLI

Track your daily expenses with categories, monthly budgets, and CSV export functionality.

> 📌 Based on the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) project from [roadmap.sh](https://roadmap.sh).

**Location:** `Expense_tracker/`

**Setup:**

**On Windows:**
```bash
cd Expense_tracker
init.bat
```

**On Linux/macOS:**
```bash
cd Expense_tracker
chmod +x init.sh run.sh
./init.sh
```

**Manual Setup:**
```bash
cd Expense_tracker
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
pip install -r requirements.txt
```

**Usage:**

**On Windows:**
```bash
run.bat add --description "Groceries" --amount 50.00 --category "Food"
run.bat list
run.bat list --category "Food"
run.bat update --id 1 --description "Supermarket" --amount 55.00
run.bat delete --id 1
run.bat summary --month 3 --budget 500.00
```

**On Linux/macOS:**
```bash
./run.sh add --description "Groceries" --amount 50.00 --category "Food"
./run.sh list
./run.sh list --category "Food"
./run.sh update --id 1 --description "Supermarket" --amount 55.00
./run.sh delete --id 1
./run.sh summary --month 3 --budget 500.00
```

**Or directly:**
```bash
python expense.py add --description "Groceries" --amount 50.00 --category "Food"
python expense.py list
python expense.py summary --month 3 --budget 500.00
```

**Operations:**
- `add` - Add a new expense (requires: `--description`, `--amount`, `--category`)
- `list` - List all expenses (optional: `--category` to filter)
- `update` - Update an expense (requires: `--id`, `--description`, `--amount`)
- `delete` - Delete an expense (requires: `--id`)
- `summary` - Get expense summary (optional: `--month` 1-12, `--budget` for budget warnings)

**Data Storage:** Expenses are stored in `expenses.json`. The app prompts to export to CSV after each operation.

---

### 3. GitHub Activity Fetcher

Fetch and display GitHub user activity events with response caching to reduce API calls.

> 📌 Based on the [GitHub User Activity](https://roadmap.sh/projects/github-user-activity) project from [roadmap.sh](https://roadmap.sh).

**Location:** `Github-User_Activity/`

**Setup:**

1. **Create a GitHub Personal Access Token:**
   - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Generate a new token with appropriate permissions
   - Copy the token

2. **Set up the environment:**

**On Windows:**
```bash
cd Github-User_Activity
init.bat
```

**On Linux/macOS:**
```bash
cd Github-User_Activity
chmod +x init.sh run.sh
./init.sh
```

3. **Create a `.env` file:**
   Create a `.env` file in the `Github-User_Activity/` folder with:
   ```
   GITHUB_TOKEN=your_github_token_here
   ```

**Note:** The `.env` file is already in `.gitignore` and won't be committed to version control.

**Usage:**

**On Windows:**
```bash
run.bat <github_username>
run.bat <github_username> <event_type>
```

**On Linux/macOS:**
```bash
./run.sh <github_username>
./run.sh <github_username> <event_type>
```

**Or directly:**
```bash
python github.py <github_username>
python github.py <github_username> <event_type>
```

**Event Types:**
- `PushEvent` - Commits pushed to repositories
- `CreateEvent` - Repositories or branches created
- `DeleteEvent` - Repositories or branches deleted
- `ForkEvent` - Repositories forked
- `MemberEvent` - Collaborators added
- `PullRequestEvent` - Pull requests opened/closed/merged

**Features:**
- Response caching for 60 seconds to reduce API calls
- Human-readable event descriptions
- Optional event type filtering

**Data Storage:** Cache is stored in `cache.json` (ignored by git).

---

### 4. Number Guessing Game

An interactive CLI game where you guess a random number between 1 and 100 with multiple difficulty levels.

> 📌 Based on the [Number Guessing Game](https://roadmap.sh/projects/number-guessing-game) project from [roadmap.sh](https://roadmap.sh).

**Location:** `Guessing-Number/`

**Setup:**
```bash
# Navigate to the project folder
cd Guessing-Number

# No virtual environment or dependencies required
```

**Usage:**
```bash
python guessing.py
```

**Game Features:**
- Three difficulty levels:
  - **Easy:** 10 attempts
  - **Medium:** 5 attempts (default)
  - **Hard:** 3 attempts
- Hints indicating if your guess is higher or lower
- Proximity warnings when you're close (within 7)
- Time tracking
- Replay option

**How to Play:**
1. Run the script
2. Select difficulty level (1, 2, or 3)
3. Guess numbers between 1 and 100
4. Get hints if your guess is wrong
5. Try to guess the number within your attempts limit
6. Play again if desired

---

### 5. GitHub Trending CLI

Fetch and display trending GitHub repositories, filtered by time range and sorted by star count.

> 📌 Based on the [GitHub Trending CLI](https://roadmap.sh/projects/github-trending-cli) project from [roadmap.sh](https://roadmap.sh).

**Location:** `Github-Trending/`

**Setup:**

**On Windows:**
```bash
cd Github-Trending
init.bat
```

**On Linux/macOS:**
```bash
cd Github-Trending
chmod +x init.sh run.sh
./init.sh
```

**Usage:**

**On Windows:**
```bash
run.bat --duration month --limit 20
```

**On Linux/macOS:**
```bash
./run.sh --duration month --limit 20
```

**Or directly:**
```bash
python trending-repos.py --duration month --limit 20
```

**Command-Line Arguments:**
- `--duration` - Time range: `day`, `week`, `month`, or `year` (default: `week`)
- `--limit` - Number of repositories to display, 1-100 (default: `10`)

**Note:** "Trending" is approximated using the GitHub Search API as repositories created within the time range, sorted by stars. No authentication required.

---

## 📝 Notes

- All projects use JSON files for local data storage
- Virtual environments are recommended for projects with dependencies
- Virtual environment folders (`venv/`) are excluded from version control via `.gitignore`
- Each project can be run independently
- The GitHub Activity Fetcher requires a valid GitHub token

---

## 🔧 Troubleshooting

### Common Issues

1. **ModuleNotFoundError:**
   - Make sure you've activated the virtual environment
   - Install dependencies: `pip install -r requirements.txt`

2. **GitHub Activity Fetcher - Token Error:**
   - Ensure `.env` file exists in `Github-User_Activity/` folder
   - Verify the token format: `GITHUB_TOKEN=your_token_here`
   - Check that the token has not expired

3. **Permission Denied (Linux/macOS):**
   - Make scripts executable: `chmod +x init.sh run.sh`

4. **Python version:**
   - Ensure Python 3.x is installed and in your PATH
   - Check version: `python --version` or `python3 --version`

---

## 📄 License

This is a collection of practice projects for learning purposes.

---

## 🤝 Contributing

Feel free to fork this repository and improve any of the projects. Each project is self-contained, making it easy to experiment and add features.
