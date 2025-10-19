# Running subprojects

## Core Python folders

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
  python python-generators-0x00/1-main.py
  ```

- Decorators

  ```bash
  python python-decorators-0x01/create_users_db.py
  python python-decorators-0x01/0-log_queries.py
  ```

- Context managers & async DB
  ```bash
  python python-context-async-perations-0x02/0-databaseconnection.py
  python python-context-async-perations-0x02/3-concurrent.py
  ```

## Django apps

### messaging_app

```bash
cd messaging_app
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Django-Middleware-0x03

```bash
cd Django-Middleware-0x03
pip install -r requirments.txt
python manage.py migrate
python manage.py runserver
```

### Django-signals_orm-0x04

```bash
cd Django-signals_orm-0x04
pip install -r requirments.txt
python manage.py migrate
python manage.py runserver
```

> [!TIP]
> For Docker/K8s examples, check manifests under `messaging_app/` and ensure you have a local cluster (kind/minikube) or a configured kubecontext.
