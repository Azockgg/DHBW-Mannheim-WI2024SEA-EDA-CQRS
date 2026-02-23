FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir flask==3.0.3

COPY . .

EXPOSE 8081
CMD ["python", "main.py"]
