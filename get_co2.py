#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from influxdb import InfluxDBClient
import mh_z19
import time

def write_to_influxDB(co2_value):
#        client = InfluxDBClient('localhost', 8086, '', '', 'thp')
        json_body = [
            {
                "measurement": "co2",
                "fields": {
                    "co2": co2_value
                }
            }
        ]
#        client.write_points(json_body)
cnt = 0
while True:
    co2_ret = mh_z19.read()
    if 'co2' in co2_ret:
        co2_value = co2_ret.get('co2')
        print("co2:" + str(co2_value))
 #       write_to_influxDB(co2_value)
        break
    if cnt >= 5:
        break
    cnt=cnt+1
    time.sleep(1)    

