FROM python:3

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install smbus2 mh_z19 schedule
COPY ./bme280-p3.py bme280-p3.py

CMD ["python","bme280-p3.py"]
