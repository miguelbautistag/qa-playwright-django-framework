# GEMINI.md - Playwright Exercise 2.0 Context & Refactoring Rules

## Project Overview
This project is an enterprise-grade QA Automation suite targeting a local Django AUT (`mysite/challenge_app`). The goal is refactoring legacy procedural test scripts into a clean, modular Page Object Model (POM) architecture using Python, Pytest, and Playwright.

---

## Technical Stack & Constraints
- **Language & Runtime:** Python 3.10+
- **Test Runner:** Pytest (`pytest-playwright`)
- **Automation Engine:** Playwright Python (Sync/Async standard pytest fixtures)
- **AUT (Application Under Test):** Local Django app (`/login`, `/dashboard`) with artificial latency in `views.py`.
- **Operating System:** Linux / Ubuntu (manage CLI commands accordingly).

---

## Target Repository Architecture
Enforce and strictly adhere to the following directory layout:

playwright-exercise2.0/
├── config/
│   └── settings.py       # Centralized URLs, default timeouts, environment configs
├── pages/
│   ├── base_page.py      # Core wrapper around Playwright Page methods
│   └── login_page.py     # Business workflows and page element encapsulation
├── tests/
│   ├── conftest.py       # Pytest fixtures (browser, page, authentication states)
│   └── test_login.py     # AAA-structured test cases
├── .gitignore            # Excludes venv/, .pytest_cache/, reports/
└── GEMINI.md             # Project context and CLI guiding rules


---

## Critical Refactoring Rules & Standards

### 1. Zero Hardcoded Waits
- **PROHIBITED:** `page.wait_for_timeout()` or `time.sleep()`.
- **REQUIRED:** Leverage Playwright's native auto-waiting assertions (`expect(locator)`).
- Handle the Django backend's dynamic latency deterministically.

### 2. Resilient Accessibility Locators
- Avoid fragile positional locators (e.g., `page.locator('button').nth(1)` or raw XPath).
- Prefer semantic, accessibility-first locators:
  - `page.get_by_role()`
  - `page.get_by_label()`
  - `page.get_by_test_id()`

### 3. Test Structure & Design Patterns
- Every test file must follow the **Arrange-Act-Assert (AAA)** pattern clearly separated with comments.
- Page objects encapsulate page element actions and assertions specific to component states.
- Tests consume page objects and shared state purely via `conftest.py` Pytest fixtures.

---

## Gemini CLI Response & Token Optimization Rules
When assisting with code generation or terminal commands in this repository, always follow these formatting constraints to save context tokens:

1. **Snippet-Only Edits:** Do not re-print entire 200-line files when making small updates. Show only modified methods, diffs, or specific functions.
2. **Concise Shell Commands:** Suggest Linux/Ubuntu CLI commands without lengthy conversational explanations.
3. **Diff/Code First:** Lead with code solutions, followed by brief bullet points explaining *why* if necessary.
4. **Clean Code Generation:** Omit unnecessary docstrings, repetitive inline comments, or verbose print statements unless strictly requested.
