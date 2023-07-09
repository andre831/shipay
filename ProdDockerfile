FROM python:3.9 AS builder

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y build-essential

RUN pip install --no-cache-dir --user -r requirements.txt

COPY . .

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app"]
