FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install flask

CMD ["python", "C:\Users\Praneel\Projects\Automated CICD Pipeline for Simulated CPU Verification\app.py"]
