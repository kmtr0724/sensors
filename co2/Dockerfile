FROM python:3-slim

RUN apt-get update && apt-get -y install gcc sudo&& apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install mh_z19 schedule influxdb
COPY ./get_co2.py get_co2.py

CMD ["python","get_co2.py"]
