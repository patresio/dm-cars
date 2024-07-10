FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app/

EXPOSE 8000

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000