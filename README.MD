# API de Gestion de Tickets

![Python](https://img.shields.io/badge/python-3.11-blue) ![Build](https://img.shields.io/badge/build-passing-brightgreen) ![Coverage](https://codecov.io/gh/Dinara-F/test_technique/branch/master/graph/badge.svg)(https://codecov.io/gh/Dinara-F/test_technique) ![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-blue)

Cette application est une API REST pour la gestion de tickets développée avec FastAPI, utilisant SQLAlchemy et SQLite en mémoire. Elle inclut des tests unitaires, des validations de type avec mypy, et des outils de qualité de code (Black, isort, flake8, pre-commit). Elle permet de créer, consulter, mettre à jour et fermer des tickets. Chaque ticket contient : `id` (UUID), `title` (str), `description` (str), `status` (enum : `open`, `stalled`, `closed`), `created_at` (datetime). L’API propose une documentation automatique via Swagger (/docs) et ReDoc (/redoc).

## Prérequis
- Python 3.11+
- Poetry

## Installation
1. Cloner le dépôt :
```bash
git clone https://github.com/USERNAME/fastapi-tickets.git
cd fastapi-tickets
```
2. Installer les dépendances avec Poetry :
```bash
poetry install
```
3. Activer l’environnement virtuel :
```bash
poetry shell
```

## Lancer l’API
```bash
uvicorn app.main:app --reload
```
L’API sera disponible sur [http://127.0.0.1:8000](http://127.0.0.1:8000). Documentation automatique : Swagger UI [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs), ReDoc [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

## Endpoints
| Méthode | URL | Description |
|----------|-----|-------------|
| POST | `/tickets/` | Créer un ticket |
| GET | `/tickets/` | Lister tous les tickets |
| GET | `/tickets/{ticket_id}` | Récupérer un ticket |
| PUT | `/tickets/{ticket_id}` | Modifier un ticket |
| PATCH | `/tickets/{ticket_id}/close` | Fermer un ticket |

## Tests
Les tests utilisent pytest et pytest-mock. Pour lancer tous les tests :
```bash
pytest
```
Pour lancer avec couverture :
```bash
pytest --cov=app --cov-report=term-missing
```

## Linter et vérification de types
Formatage avec Black :
```bash
poetry run black app tests
```
Organisation des imports avec isort :
```bash
poetry run isort app tests
```
Linter avec flake8 :
```bash
poetry run flake8 app tests
```
Vérification des types avec mypy :
```bash
poetry run mypy app tests
```

## Structure du projet
```
.
├── README.MD
├── app
│   ├── __init__.py
│   ├── db.py
│   ├── main.py
│   └── tickets
│       ├── __init__.py
│       ├── models.py
│       ├── repository.py
│       ├── routers.py
│       └── schemas.py
├── mypy.ini
├── poetry.lock
├── pyproject.toml
├── tests
│   ├── __init__.py
│   └── tickets
│       ├── __init__.py
│       ├── conftest.py
│       ├── test_api.py
│       └── test_repo.py
└── tickets.db
```

## Pre-commit
Pour activer les hooks de qualité de code :
```bash
poetry run pre-commit install
```
Les hooks exécutent Black, isort, flake8 et mypy avant chaque commit.


