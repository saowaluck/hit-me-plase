FROM python:3.7-alpine

RUN pip install Django==2.2.1 \
    entrypoints==0.3 \
    flake8==3.7.7 \
    mccabe==0.6.1 \
    pycodestyle==2.5.0 \
    pyflakes==2.1.1 \
    pytz==2019.1 \
    sqlparse==0.3.0 \
    yapf==0.27.0

COPY . /app/
WORKDIR /app/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["sh", "-c", "cd hit_me_plase && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
