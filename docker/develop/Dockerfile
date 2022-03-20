FROM python:3.8-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./requirements-dev.txt /code/requirements-dev.txt

RUN pip install --upgrade pip
RUN pip install -r /code/requirements-dev.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]