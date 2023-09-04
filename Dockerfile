FROM python:3.10

RUN mkdir /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
WORKDIR /code/django_auth
CMD gunicorn django_auth.wsgi:application --bind 0.0.0.0:8000