# Build frontend
FROM node:16 AS frontend-builder
WORKDIR /frontend
COPY frontend .
RUN yarn install
RUN yarn build

# Build backend
FROM python:3-slim-bullseye
WORKDIR /app
COPY backend backend
COPY --from=frontend-builder /frontend/webpack-stats.json frontend/webpack-stats.json
COPY --from=frontend-builder /frontend/dist frontend/dist
RUN pip install --no-cache-dir -r backend/requirements.txt
WORKDIR /app/backend
ENV CONFIG_DIR=/config
ENV ENV_NAME=production
RUN env SECRET_KEY="empty" DOMAIN="empty" AUTH_HEADER="empty" python3 manage.py collectstatic
CMD [ "gunicorn", "project.wsgi" ]
LABEL org.opencontainers.image.source https://github.com/uscsd/usc-program-of-studies
