# ALX Backend Python

Advanced Python backend exercises and mini-projects: type hints, async IO, comprehensions, testing, decorators, generators, and Django apps.

> [!NOTE]
> This repo is a monorepo of multiple, mostly independent subprojects. You can work on each folder standalone. See the docs below for setup and how to run specific parts.

## Repository map

- Core Python topics

  - `0x00-python_variable_annotations` — type hints and annotations. See folder README.
  - `0x01-python_async_function` — async/await and concurrency.
  - `0x02-python_async_comprehension` — async generators and comprehensions.
  - `0x03-Unittests_and_integration_tests` — unit/integration testing with `unittest` (pytest optional).
  - `python-generators-0x00` — generators, streaming data from a DB.
  - `python-decorators-0x01` — practical decorators (logging, retries, transactions, caching).
  - `python-context-async-perations-0x02` — context managers and async DB operations with aiosqlite.

- Django apps and APIs
  - `messaging_app` — DRF-based messaging service; includes Docker and K8s manifests.
  - `Django-Middleware-0x03` — Django app showing middleware/logging patterns.
  - `Django-signals_orm-0x04` — Django app focusing on signals and ORM usage.

Each folder contains its own README with details, code, and examples.

## Quick start

You can use a single Python environment at the repo root or separate envs per subproject.

Prerequisites:

- Python 3.10+
- Optional: Docker (for `messaging_app`), Kubernetes cluster or kind/minikube to try manifests

### Option A — Virtualenv + pip (works everywhere)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirments.txt
```

> [!TIP]
> The root `requirments.txt` contains shared libs for exercises (e.g., `aiosqlite`, `requests`, MySQL connector). Some folders (Django apps) also provide their own `requirements` files — install those when working inside those folders.

### Option B — uv (if you prefer pyproject/lock workflows)

This repo includes a `pyproject.toml` used primarily by Django examples. If you use `uv`:

```bash
uv sync
```

## Run a few examples

- Variable annotations

  ```bash
  python 0x00-python_variable_annotations/0-add.py
  ```

- Async functions

  ```bash
  python 0x01-python_async_function/2-measure_runtime.py
  ```

- Async comprehensions

  ```bash
  python 0x02-python_async_comprehension/2-measure_runtime.py
  ```

- Generators (DB streaming)

  ```bash
  # Requires access to a MySQL instance; see that folder README for connection details
  python python-generators-0x00/1-main.py
  ```

- Decorators (create a local SQLite db and run examples)

  ```bash
  python python-decorators-0x01/create_users_db.py
  python python-decorators-0x01/0-log_queries.py
  ```

- Context managers & async DB

  ```bash
  python python-context-async-perations-0x02/0-databaseconnection.py
  python python-context-async-perations-0x02/3-concurrent.py
  ```

- Django apps (example)
  ```bash
  cd messaging_app
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
  ```

> [!IMPORTANT]
> SQLite databases stored in the repo folders are for local experimentation only. Delete and recreate them freely (`*.sqlite3`). Always run `migrate` before starting a Django app.

## Testing

- Standard library `unittest` is used in `0x03-Unittests_and_integration_tests`:

  ```bash
  python -m unittest discover 0x03-Unittests_and_integration_tests -v
  ```

- Pytest is available as a dev dependency via `pyproject.toml` if you prefer:
  ```bash
  pytest -q
  ```

## Documentation

- Project overview: [docs/overview.md](docs/overview.md)
- Environment setup: [docs/setup.md](docs/setup.md)
- How to run each subproject: [docs/running.md](docs/running.md)
- Testing guide: [docs/testing.md](docs/testing.md)
- Troubleshooting: [docs/troubleshooting.md](docs/troubleshooting.md)

## Notes

- Subprojects are intentionally lightweight and independent; feel free to open just one folder in your editor to focus on a topic.
- Many folders include a dedicated README with more targeted instructions — start there when in doubt.
