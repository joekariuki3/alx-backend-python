# Testing guide

## unittest (standard library)

Run tests for the testing exercises:

```bash
python -m unittest discover 0x03-Unittests_and_integration_tests -v
```

## pytest (optional)

Pytest is available as a dev dependency via `pyproject.toml`:

```bash
pytest -q
```

> [!NOTE]
> If you use a per-folder virtual environment, make sure it is activated before running tests.
