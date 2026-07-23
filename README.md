````md
# Playwright & Pytest Automation Framework

This repository contains an end-to-end test automation framework for a Django application using **Python**, **Playwright (Sync API)**, and **Pytest**.

The project started from a simple procedural test and was gradually refactored into a cleaner and more maintainable automation framework following the **Page Object Model (POM)**. The main focus was writing tests that are easy to understand, reliable to execute, and simple to extend as the application grows.

---

# Project Structure

```text
playwright-exercise2.0/
├── e2e_tests/
│   ├── config/
│   │   └── settings.py       # Runtime configuration
│   ├── pages/
│   │   ├── base_page.py      # Shared Playwright actions
│   │   └── login_page.py     # Login page objects and flows
│   ├── tests/
│   │   ├── conftest.py       # Pytest fixtures
│   │   └── test_login.py     # Login test scenarios
│   └── pytest.ini            # Pytest configuration
├── mysite/
│   ├── challenge_app/
│   ├── db.sqlite3
│   └── manage.py
├── requirements.txt
└── README.md
```

---

# Design Decisions

A few principles guided the implementation of this project:

- **Page Object Model (POM)** keeps page interactions separated from the test logic, making the tests easier to read and maintain.
- **Playwright's built-in waiting mechanisms** replace explicit sleeps whenever possible, resulting in more stable and predictable test execution.
- **Accessible and stable locators** (`get_by_role()`, `get_by_label()`, IDs) are preferred over brittle selectors based on indexes or CSS hierarchy.
- **Arrange – Act – Assert (AAA)** is used consistently to keep each test focused on a single behavior.
- **Pytest fixtures** handle browser setup and teardown so each test runs independently.

The goal wasn't simply to make the tests pass, but to create a framework that someone else could easily pick up and continue working on.

---

# Tech Stack

- Python 3.11+
- Playwright (Sync API)
- Pytest
- pytest-playwright
- Django 5.2
- SQLite

---

# Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/luidcrua/playwright-exercise.git
cd playwright-exercise2.0
```

## 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

---

# Running the Django Application

Open a new terminal and activate the virtual environment.

```bash
source venv/bin/activate
cd mysite
```

Run the database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/login
```

---

# Running the Test Suite

From another terminal:

```bash
source venv/bin/activate
```

Run all tests:

```bash
PYTHONPATH=. pytest e2e_tests/tests
```

Run in headed mode:

```bash
PYTHONPATH=. pytest e2e_tests/tests --headed
```

Keep Playwright traces when a test fails:

```bash
PYTHONPATH=. pytest e2e_tests/tests --tracing=retain-on-failure
```

---

# Debugging Failures

When a test fails, Playwright stores a trace that can be opened locally.

```bash
playwright show-trace test-results/<test-run-folder>/trace.zip
```

The trace viewer makes it much easier to understand what happened during execution by showing every browser action, network request, screenshot, and DOM snapshot.

---

# Test Coverage

| Test | Description |
|------|-------------|
| `test_successful_login_redirects_to_dashboard` | Verifies that a valid user can log in successfully and is redirected to the dashboard. |
| `test_login_with_invalid_credentials_stays_on_login` | Verifies that invalid credentials keep the user on the login page and do not display authenticated content. |

---

# What I Focused On

Rather than trying to build a large framework, I focused on writing automation that would still be easy to maintain a few months from now.

Some areas I paid particular attention to include:

- Writing readable tests with minimal duplication.
- Keeping page logic separate from test assertions.
- Using reliable locator strategies instead of fragile selectors.
- Letting Playwright handle synchronization instead of relying on manual waits.
- Building a project structure that can grow as additional pages and test scenarios are added.

While this is a relatively small project, the same structure can be extended to larger applications without requiring significant changes to the overall architecture.
````
