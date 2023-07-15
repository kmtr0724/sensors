FROM python:3-slim

RUN apt-get update && apt-get -y install gcc sudo systemctl && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install mh_z19 schedule influxdb
COPY ./get_co2.py get_co2.py
COPY ./get_co2_test.py get_co2_test.py
COPY ./serial-getty@.service /lib/systemd/system/serial-getty@.service

CMD ["python","get_co2.py"]
