# Troubleshooting

## Common issues

> [!WARNING]
> Many scripts assume an active virtual environment. If imports fail, ensure your venv is activated and dependencies are installed.

- Import errors

  - Re-activate your venv: `source .venv/bin/activate`
  - Install deps: `pip install -r requirments.txt` (root) or the subproject's `requirements.txt`

- Django migrations

  - Delete local `db.sqlite3` if corrupt and re-run: `python manage.py migrate`
  - Ensure `INSTALLED_APPS` and settings match the app you are running

- MySQL connection (generators folder)

  - Verify `.env` variables and that the server is reachable
  - Confirm `mysql-connector-python` is installed

- Async scripts hang
  - Look for blocking calls inside async functions
  - Use `asyncio.run(...)` and avoid mixing event loops

## Getting help

- Check the subproject README first
- Open an issue with the exact command and full traceback
