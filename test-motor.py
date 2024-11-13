import RPi.GPIO as GPIO
from time import sleep

motor1 = 17
motor2 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor2, GPIO.OUT)


def forward():
    print('forward')
    GPIO.output(motor1, GPIO.HIGH)
    GPIO.output(motor2, GPIO.LOW)
    sleep(1)
    GPIO.output(motor1, GPIO.LOW)
    GPIO.output(motor2, GPIO.LOW)


def backward():
    print('backward')
    GPIO.output(motor1, GPIO.LOW)
    GPIO.output(motor2, GPIO.HIGH)
    sleep(1)
    GPIO.output(motor1, GPIO.LOW)
    GPIO.output(motor2, GPIO.LOW)


try:
    while True:
        forward()
        sleep(1)
        backward()
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
