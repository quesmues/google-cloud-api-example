FROM python:3.10

RUN apt-get update
RUN apt-get clean

COPY app/ /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

ENV PORT 8000

CMD exec uvicorn app.main:app --host 0.0.0.0 --port $PORT
