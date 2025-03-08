FROM python:3.9-slim
WORKDIR /app
COPY run.py .
CMD ["python", "run.py"]