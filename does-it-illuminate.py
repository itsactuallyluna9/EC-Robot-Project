import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pins = [12, 16, 20, 21]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

try:
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.5)  # Keep it on for half a second
        GPIO.output(pin, GPIO.LOW)
finally:
    GPIO.cleanup()
