import RPi.GPIO as GPIO
import time


right_motor_a = 24
right_motor_b = 23
right_motor_en = 25

left_motor_a = 15
left_motor_b = 14
left_motor_en = 4


GPIO.setmode(GPIO.BCM)

GPIO.setup(right_motor_a , GPIO.OUT)
GPIO.setup(right_motor_b , GPIO.OUT)
GPIO.setup(right_motor_en , GPIO.OUT)

GPIO.setup(left_motor_a , GPIO.OUT)
GPIO.setup(left_motor_b , GPIO.OUT)
GPIO.setup(left_motor_en , GPIO.OUT)

pwm_r = GPIO.PWM(right_motor_en , 1000 )
pwm_l = GPIO.PWM(left_motor_en , 1000 )

pwm_r.start(75)
pwm_l.start(75)

def forward(second):
    print("forward Moving ")
    GPIO.output(right_motor_a,GPIO.HIGH)
    GPIO.output(right_motor_b,GPIO.LOW)
    GPIO.output(left_motor_a,GPIO.HIGH)
    GPIO.output(left_motor_b,GPIO.LOW)
    time.sleep(second)

def reverse(second):
    print("Reverse Moving ")
    GPIO.output(right_motor_a,GPIO.LOW)
    GPIO.output(right_motor_b,GPIO.HIGH)
    GPIO.output(left_motor_a,GPIO.LOW)
    GPIO.output(left_motor_b,GPIO.HIGH)
    time.sleep(second)


def right(second):
    print("Left Moving ")
    GPIO.output(right_motor_a,GPIO.LOW)
    GPIO.output(right_motor_b,GPIO.HIGH)
    GPIO.output(left_motor_a,GPIO.HIGH)
    GPIO.output(left_motor_b,GPIO.LOW)
    time.sleep(second)

def left(second):
    print("Right Moving ")
    GPIO.output(right_motor_a,GPIO.HIGH)
    GPIO.output(right_motor_b,GPIO.LOW)
    GPIO.output(left_motor_a,GPIO.LOW)
    GPIO.output(left_motor_b,GPIO.HIGH)
    time.sleep(second)

def stop():
    print("Stopping Motors")
    pwm_r.ChangeDutyCycle(0)
    pwm_l.ChangeDutyCycle(0)

def exit_():
    GPIO.cleanup()

def main():
    forward(2)
    reverse(2)
    left(2)
    right(2)
    stop()
    exit_()

if __name__ == '__main__':
    main()

