FROM python:3-slim

RUN apt-get update && apt-get -y install gcc && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install smbus2 schedule influxdb
COPY ./bme280-p3.py bme280-p3.py

CMD ["python","bme280-p3.py"]
