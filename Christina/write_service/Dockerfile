FROM python:3.9-slim

WORKDIR /feeding-command-service

# Abhängigkeiten kopieren & installieren
RUN pip install --no-cache-dir flask pika flask-cors

# Code kopieren
COPY . .

# Service starten 
CMD ["python", "feeding-command-service.py"]