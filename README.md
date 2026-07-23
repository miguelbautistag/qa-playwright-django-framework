# 🚀 Playwright & Pytest Automation Framework

An end-to-end test automation framework for a Django application built with **Python**, **Playwright (Sync API)**, and **Pytest**.

The project began as a single procedural test and was refactored into a more maintainable and scalable framework using the **Page Object Model (POM)**. The goal was to build automation that is easy to read, reliable to execute, and straightforward to extend as new test scenarios are introduced.

---

## 📑 Table of Contents

- [Project Structure](#-project-structure)
- [Design Decisions](#-design-decisions)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Running the Application](#-running-the-django-application)
- [Running the Tests](#-running-the-test-suite)
- [Debugging](#-debugging-failures)
- [Test Coverage](#-test-coverage)
- [Key Takeaways](#-what-i-focused-on)

---

## 📁 Project Structure

```text
playwright-exercise2.0/
├── e2e_tests/
│   ├── config/
│   │   └── settings.py
│   ├── pages/
│   │   ├── base_page.py
│   │   └── login_page.py
│   ├── tests/
│   │   ├── conftest.py
│   │   └── test_login.py
│   └── pytest.ini
├── mysite/
│   ├── challenge_app/
│   ├── db.sqlite3
│   └── manage.py
├── requirements.txt
└── README.md
```

### Folder Overview

| Folder | Purpose |
|---------|---------|
| `config/` | Centralized project configuration |
| `pages/` | Page Object classes and UI interactions |
| `tests/` | Test scenarios written with Pytest |
| `conftest.py` | Shared fixtures and browser setup |
| `mysite/` | Django application under test |

---

## 🏗️ Design Decisions

The framework follows a few simple principles that help keep the codebase maintainable.

✅ **Page Object Model**

Keeps UI interactions separated from test logic, making both easier to maintain.

✅ **Playwright Auto-Waiting**

Relies on Playwright's built-in synchronization instead of manual `sleep()` calls.

✅ **Stable Locators**

Uses semantic locators whenever possible:

- `get_by_role()`
- `get_by_label()`
- IDs
- Accessible selectors

instead of brittle CSS or positional selectors.

✅ **Arrange – Act – Assert**

Each test follows the AAA pattern to improve readability.

✅ **Reusable Fixtures**

Pytest fixtures handle browser lifecycle and test isolation.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11+ | Programming language |
| Playwright | Browser automation |
| Pytest | Test runner |
| pytest-playwright | Playwright integration |
| Django 5.2 | Application under test |
| SQLite | Database |

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/luidcrua/playwright-exercise.git
cd playwright-exercise2.0
```

---

## 2️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

---

# ▶️ Running the Django Application

Activate the virtual environment:

```bash
source venv/bin/activate
```

Navigate to the Django project:

```bash
cd mysite
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/login
```

---

# 🧪 Running the Test Suite

Run all tests:

```bash
PYTHONPATH=. pytest e2e_tests/tests
```

Run with the browser visible:

```bash
PYTHONPATH=. pytest e2e_tests/tests --headed
```

Keep Playwright traces after failures:

```bash
PYTHONPATH=. pytest e2e_tests/tests --tracing=retain-on-failure
```

---

# 🔍 Debugging Failures

If a test fails, Playwright automatically generates a trace file.

Open it with:

```bash
playwright show-trace test-results/<test-run-folder>/trace.zip
```

The Trace Viewer provides:

- Timeline of executed actions
- Screenshots
- DOM snapshots
- Network requests
- Console logs

which makes reproducing and debugging failures much easier.

---

## ✅ Test Coverage

| Test Case | Purpose |
|------------|---------|
| `test_successful_login_redirects_to_dashboard` | Confirms that valid credentials successfully authenticate the user and redirect them to the dashboard. |
| `test_login_with_invalid_credentials_stays_on_login` | Confirms that invalid credentials do not authenticate the user and the login page remains displayed. |

---

# 💭 What I Focused On

Instead of building a large framework, I focused on building one that is clean, maintainable, and easy to extend.

Some of the areas I paid the most attention to were:

- Keeping tests concise and readable.
- Reducing duplicated code through reusable page objects.
- Using reliable locator strategies.
- Letting Playwright manage synchronization whenever possible.
- Organizing the project so additional pages and tests can be added with minimal effort.

Although this project is intentionally small, the same structure can be scaled to larger applications without requiring major architectural changes.
