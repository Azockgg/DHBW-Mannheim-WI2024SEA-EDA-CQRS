FROM python:3.9-slim

WORKDIR /cat-stats-query-service

# Abhängigkeiten kopieren & installieren
RUN pip install --no-cache-dir flask pika flask-cors

# Code kopieren
COPY . .

# Service starten
CMD ["python", "cat-stats-query-service.py"]