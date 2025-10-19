# Project overview

This monorepo bundles several Python backend mini-projects and Django apps. Each folder is self-contained and can be run independently.

## Top-level layout

- Core Python topics

  - `0x00-python_variable_annotations` — type hints and annotations
  - `0x01-python_async_function` — async/await and concurrency
  - `0x02-python_async_comprehension` — async generators and comprehensions
  - `0x03-Unittests_and_integration_tests` — unit and integration testing
  - `python-generators-0x00` — generators and DB streaming
  - `python-decorators-0x01` — decorators for logging, retries, transactions, caching
  - `python-context-async-perations-0x02` — context managers and async DB operations

- Django apps
  - `messaging_app` — DRF-based messaging service (with Docker/K8s manifests)
  - `Django-Middleware-0x03` — middleware and request logging examples
  - `Django-signals_orm-0x04` — Django signals and ORM patterns

> [!TIP]
> Start from a folder README to see its specific goals, dependencies, and run commands.
