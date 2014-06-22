#!/usr/bin/python

import Adafruit_BBIO.ADC as ADC
import time
import math


class probe:
    def __init__(self, adc_pin):
        ADC.setup()
        self.adc_pin = adc_pin

    def readTemp(self):
        # From the datasheet
        bvalue = 3950
        r_bias = 10000
        # solved using 10k for r_therm and 25 for temp_c
        r_alpha = 0.017633
        c_to_k = 273.15

        adcValue = ADC.read(self.adc_pin)
        r_therm  = ((1/adcValue)-1)*r_bias
        temp_c = (10*((bvalue/(math.log(r_therm/r_alpha)))-c_to_k))/10
        return temp_c

def get_f(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f

myProbe = probe('P9_36')

while True:
    temp_c = myProbe.readTemp()
    temp_f = get_f(temp_c)
    print 'temp_c=', temp_c, '  temp_f=', temp_f
    time.sleep(1)

