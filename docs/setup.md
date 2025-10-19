# Environment setup

## Requirements

- Python 3.10+
- pip (or uv)
- Optional: Docker, Kubernetes tooling (for `messaging_app`)

## Root environment (shared libs for exercises)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirments.txt
```

> [!NOTE]
> Some subprojects (especially Django apps) have their own `requirements.txt` or use the root `pyproject.toml`. Activate your env first, then install per-folder requirements when working in that folder.

## Using uv (optional)

```bash
# sync dependencies from pyproject.toml / uv.lock
uv sync
```

## Database notes

- SQLite files checked in are for demos only; recreate as needed.
- `python-generators-0x00` expects a MySQL instance; see that folder README for connection details and `.env` variables.
