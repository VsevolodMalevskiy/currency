FROM python:3.9.10

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD python ./app/manage.py runserver 0.0.0.0:8000
