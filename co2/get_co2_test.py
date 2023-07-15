#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mh_z19
import time
import schedule
import os

def get_co2_value():
    cnt = 0
    while True:
        #co2_ret = mh_z19.read(serial_console_untouched=True)
        co2_ret = mh_z19.read()
        if 'co2' in co2_ret:
            co2_value = co2_ret.get('co2')
            print("co2:" + str(co2_value))
            break
        if cnt >= 5:
            break
        cnt=cnt+1
        time.sleep(3)    

get_co2_value()
