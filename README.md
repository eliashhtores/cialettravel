# cialettravel

Runnable full stack travel agency app with:

- **Backend**: Django + Django REST Framework
- **Data**: SQLite by default, PostgreSQL via environment variables / Docker Compose
- **Frontend**: Static Tailwind-based landing page rendered by Django templates
- **Local orchestration**: Docker Compose (`web` + `db`)

## Local run (without Docker)

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

App URLs:

- Home page: `http://127.0.0.1:8000/`
- Destinations API: `http://127.0.0.1:8000/api/destinations/`
- Packages API: `http://127.0.0.1:8000/api/packages/`

## Docker Compose run (PostgreSQL-backed)

```bash
cp .env.example .env
# Edit .env and set DJANGO_SECRET_KEY and other values
docker compose up --build
```

Then open `http://localhost:8000/`.
