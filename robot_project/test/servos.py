from ..physical import Servo, SERVO_1, SERVO_2

if __name__ == "__main__":
    print("--Testing servos!--")
    
    print("Servo 1")
    servo1 = Servo(SERVO_1)
    print("Rotating 90 degrees clockwise")
    servo1.rotate(90)
    print("Rotating 90 degrees counter-clockwise")
    servo1.rotate(-90)
    print("Rotating 360 degrees clockwise")
    servo1.rotate(360)
    print("Rotating 360 degrees counter-clockwise")
    servo1.rotate(-360)

    print("Servo 2")
    servo2 = Servo(SERVO_2)
    print("Rotating 90 degrees clockwise")
    servo2.rotate(90)
    print("Rotating 90 degrees counter-clockwise")
    servo2.rotate(-90)
    print("Rotating 360 degrees clockwise")
    servo2.rotate(360)
    print("Rotating 360 degrees counter-clockwise")
    servo2.rotate(-360)

    print("--Servo test done!--")
