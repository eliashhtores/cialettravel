# Build stage: compile Tailwind CSS
FROM node:20-slim AS frontend
WORKDIR /frontend
COPY package.json ./
RUN npm install
COPY tailwind.config.js ./
COPY templates/ ./templates/
COPY static/css/app.css ./static/css/app.css
RUN npx tailwindcss -i static/css/app.css -o static/css/tailwind.min.css --minify

# Build stage: compile psycopg2 against system libpq
FROM python:3.12-slim AS python-builder
WORKDIR /build
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Final stage
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
# Runtime libpq shared library (required by psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends libpq5 \
    && rm -rf /var/lib/apt/lists/*
COPY --from=python-builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY . .
COPY --from=frontend /frontend/static/css/tailwind.min.css static/css/tailwind.min.css
RUN addgroup --system app && adduser --system --ingroup app app
RUN chown -R app:app /app
USER app
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "cialettravel.wsgi:application"]
