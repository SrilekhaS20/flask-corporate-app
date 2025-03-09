# Build Stage
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Production Stage
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
RUN pip show gunicorn
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]