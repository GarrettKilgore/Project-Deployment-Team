FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Optional: Re-seed DB with dummy data during build (assumes dummydb.py is idempotent)
RUN python dummydb.py

EXPOSE 5000
CMD ["python", "app.py"]
