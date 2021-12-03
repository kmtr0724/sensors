#!/usr/bin/env python
# -*- coding: utf-8 -*-
from influxdb import InfluxDBClient
import mh_z19

def write_to_influxDB(co2_value):
        client = InfluxDBClient('localhost', 8086, '', '', 'thp')
        json_body = [
            {
                "measurement": "co2",
                "fields": {
                    "co2": co2_value
                }
            }
        ]
        client.write_points(json_body)
co2_ret = mh_z19.read()
co2_value = co2_ret.get('co2')
write_to_influxDB(co2_value)

