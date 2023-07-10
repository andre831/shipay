FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

COPY . .

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app

COPY src /app

RUN pip install --no-cache-dir gunicorn

ENV FLASK_APP=app.py

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]