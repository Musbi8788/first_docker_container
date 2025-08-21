FROM python:3

COPY . /main

WORKDIR /main

CMD python main.py