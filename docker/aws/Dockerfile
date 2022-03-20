FROM public.ecr.aws/lambda/python:3.8

COPY ./app ./app

COPY ./requirements.txt ./

RUN chmod a+rw ./app ./app/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["app.main.handler"]