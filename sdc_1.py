import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)
Trig = 14
Echo = 15
Motor1 = 18
Motor2 = 23
Motor3 = 24
Motor4 = 25

GPIO.setup(Motor1, GPIO.OUT)
GPIO.setup(Motor2, GPIO.OUT)
GPIO.setup(Motor3, GPIO.OUT)
GPIO.setup(Motor4, GPIO.OUT)
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

try:
    while True:

        GPIO.output(Trig, False)
        time.sleep(1)
        GPIO.output(Trig, True)
        time.sleep(0.00001)
        GPIO.output(Trig, False)

        while GPIO.input(Echo) == False:
            end = time.time()

        while GPIO.input(Echo) == True:
            start = time.time()

        sig_time = start-end
        distance = 165*100*sig_time

        if(distance > 20.0):

            GPIO.output(Motor1, GPIO.LOW)
            GPIO.output(Motor2, GPIO.HIGH)
            GPIO.output(Motor3, GPIO.LOW)
            GPIO.output(Motor4, GPIO.HIGH)
            print('Forward')

        else:

            GPIO.output(Motor1, GPIO.LOW)
            GPIO.output(Motor2, GPIO.LOW)
            GPIO.output(Motor3, GPIO.LOW)
            GPIO.output(Motor4, GPIO.LOW)
            time.sleep(0.1)
            print('Stop')

        print('distance from object is:() cm', format(distance))

except KeyboardInterrupt:

    GPIO.cleanup()
