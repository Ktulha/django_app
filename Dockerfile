FROM python:3.12-alpine

WORKDIR /app

COPY ./app .

COPY ./requirements.txt .

COPY ./run.sh .

RUN pip install -r requirements.txt --force-reinstall

ENV PYTHONUNBUFFERED=1

CMD ["sh","run.sh"]

