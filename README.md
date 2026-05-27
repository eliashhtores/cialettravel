# cialettravel

Runnable full stack travel agency app with:

- **Backend**: Django + Django REST Framework (API only — no template rendering)
- **Data**: SQLite by default, PostgreSQL via environment variables / Docker Compose
- **Frontend**: Static HTML5/CSS3/Vanilla JS under `frontend/` — fetches data from the REST API via XHR
- **Local orchestration**: Docker Compose (`web` + `db`)

## Project structure

```
frontend/
  index.html          # landing page (served at / via Whitenoise)
  css/
    index.css         # component styles
    tailwind.min.css  # compiled Tailwind output
  js/
    index.js          # XHR calls to /api/destinations/ and /api/packages/
trips/                # Django app — models, serializers, API viewsets only
cialettravel/         # Django project settings, URLs
```

## Local run (without Docker)

```bash
cp .env.example .env
# In .env, set DJANGO_DEBUG=true (enables the dev-only SECRET_KEY fallback)
export $(grep -v '^#' .env | xargs)
pip install -r requirements.txt
npm install && npm run build:css   # compile Tailwind CSS (requires Node ≥ 18)
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
# Edit .env: set DJANGO_SECRET_KEY to a real secret and DJANGO_DEBUG=false
docker compose up --build
```

Then open `http://localhost:8000/`.
