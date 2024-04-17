FROM python:3

WORKDIR /

COPY server.py /server.py

RUN pip install mysql-connector-python && pip install py-mon

CMD [ "python", "./server.py" ]