FROM python:3.10

RUN apt-get update
RUN apt-get install -y awscli
RUN apt-get clean

COPY app/ /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0" ]
