# Technical Audit & Backlog: Python ToDo CLI

## 1. Original Technical Issues Identified
During code review and static analysis of the initial script (`پروژه پایانی-نسخه نهایی.py`), the following defects and edge cases were discovered:

| ID | Issue Description | Severity | Status |
| :--- | :--- | :--- | :--- |
| **BUG-01** | **Negative Index Deletion Vulnerability**: Entering task number `0` computed `number = 0 - 1 = -1`. In Python, `list.pop(-1)` silently deletes the last task in the list instead of rejecting the invalid index. | High | Fixed |
| **BUG-02** | **RTL Parentheses Typo**: The prompt string `اولویت )بالا/متوسط/پایین(: ` contained inverted parentheses, causing display glitch in RTL/LTR terminals. | Low | Fixed |
| **BUG-03** | **Empty Task Creation**: Submitting an empty task name created blank records in the persistent CSV file without validation. | Medium | Fixed |
| **BUG-04** | **Fragile CSV Deserialization**: `row[0], row[1], row[2]` indexing crashed with `IndexError` when reading empty or malformed CSV rows. | Medium | Fixed |

---

## 2. Technical Debt & Backlog (To-Do Later)
Features, architecture upgrades, and technical debt earmarked for future sprints:

- [ ] **Task Status Flag**: Introduce task completion states (`Pending`, `In-Progress`, `Completed`) rather than permanent deletion.
- [ ] **Due Date & Timestamps**: Add `created_at` and `due_date` fields using the `datetime` standard library.
- [ ] **Search & Filtering**: Allow filtering tasks by priority level (`High`, `Medium`, `Low`) or keyword substring.
- [ ] **Database Integration**: Provide an SQLite backend option (`sqlite3`) as a scalable alternative to flat CSV files.
- [ ] **Terminal UI Styling**: Add ANSI escape colors or integrate `rich` for formatted tables in the CLI.
- [ ] **CLI Arguments**: Support non-interactive CLI flags (e.g., `todo add "task" --priority high` using `argparse`).
