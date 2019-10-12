#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

#IO17 outp LOW,close the fan
GPIO.output(17, GPIO.LOW)
