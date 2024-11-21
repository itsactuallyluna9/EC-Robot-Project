from time import sleep
import RPi.GPIO as GPIO

MOTOR_1 = 17
MOTOR_2 = 22

SERVO_1 = [6, 13, 19, 26]
SERVO_2 = [12, 16, 20, 21]

SERVO_STEP_WAIT = 0.002
SERVO_STEP_SEQ = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]

SERVO_ONE_STEP_DEGREE = 5.625*(1/64) # 5.625/64 degrees per step

class Motor:
    def __init__(self, pin: int):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    # i... need to put the motor control logic here, still.

class Servo:
    def __init__(self, pins: list[int]):
        self.pins = pins
        self.step = 0
        self.degree = 0
    
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
    
    def _step(self, clockwise: bool):
        if clockwise:
            self.step = (self.step + 1) % 8
            self.degree += SERVO_ONE_STEP_DEGREE
        else:
            self.step = (self.step - 1) % 8
            self.degree -= SERVO_ONE_STEP_DEGREE
        
        for i in range(4):
            GPIO.output(self.pins[i], SERVO_STEP_SEQ[self.step][i])
        
        sleep(SERVO_STEP_WAIT)
    
    def rotate(self, degrees: float):
        steps = int(degrees / SERVO_ONE_STEP_DEGREE)
        clockwise = True if steps > 0 else False
        steps = abs(steps)
        
        for _ in range(steps):
            self._step(clockwise)
    
    def reset(self):
        self.rotate(-self.degree) # reset to "initial" position
