This repository is a minimal Python learning workspace. These instructions guide AI coding agents how to be immediately productive.

Repository snapshot
- Single script: `lab1.py` — a small interactive script that reads two integers and prints their sum and difference.

How this project is typically run
- Run locally with the system Python. Example (PowerShell):
  - `python .\lab1.py`

What to expect when editing
- `lab1.py` uses `input()` and `print()` and is intended as an educational script.
- Changes should preserve a simple, beginner-friendly interface unless the user asks to refactor.

Common, discoverable patterns
- Interactive I/O: Functions should accept parameters and return values when refactoring for testability.
  - Example: extract logic into `def add_and_subtract(a: int, b: int) -> tuple[int, int]`.
- Use f-strings for output (already used in `lab1.py`). Keep this style for new prints.

Suggested safe edits (examples you can perform without asking):
- Add input validation to `lab1.py` (handle non-integer input with a friendly message).
- Refactor core logic into functions and add a `if __name__ == "__main__":` guard.
- Add a small test scaffold using `unittest` or `pytest` and demonstrate expected behavior for `add` and `subtract`.

What not to change without confirmation
- Do not change the intended user-facing prompts or outputs unless requested — learners may rely on exact prompt text.

Developer workflows & debugging notes
- There are no build files or automated tests in this repo. After edits, run the script directly to sanity-check behavior.
- Use PowerShell on Windows: `python .\lab1.py`; to run tests (if added): `pytest` or `python -m unittest`.

Integration points and dependencies
- There are no external dependencies; avoid adding new libraries unless the user requests them.

If you need to expand the project
- Ask before introducing package management (`requirements.txt`/`pyproject.toml`) or CI.
- Propose changes as small, reversible commits and include examples how to run them.

Examples of explicit prompts that work well
- "Refactor `lab1.py` to extract `add_and_subtract(a,b)` and add unit tests using `unittest`. Keep CLI prompts identical." 
- "Add robust input validation to `lab1.py` and include a short usage note at top of the file."

When in doubt
- Ask the user whether the goal is pedagogical clarity (keep interactive prompts) or production-grade code (refactor, add tests and CLI).
