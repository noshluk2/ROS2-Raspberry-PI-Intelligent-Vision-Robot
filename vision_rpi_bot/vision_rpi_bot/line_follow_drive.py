#!/usr/bin/env python3


import rclpy
import RPi.GPIO as GPIO
from rclpy.node import Node
from std_msgs.msg import Int16

class drive_rpi(Node):

    def __init__(self):
        super().__init__('Visionbot_driver')
        self.error_value_subscriber = self.create_subscription(Int16, '/line_following_error',self.car_drive_cb, 10)
        self.motor_obj=setup(24,23,25,15,14,4)
        self.base_speed = 26 # duty cycle value
        self.right_wheel_vel  = 0
        self.left_wheel_vel = 0

    def car_drive_cb(self,error_value):
        # print("Error ->" , error_value.data)
        if(error_value.data < 0 ) : # positive case for counter clock wise rotation
            self.right_wheel_vel  = self.base_speed - 10
            self.left_wheel_vel = self.base_speed + 10
        else: # negative case for clock wise
            self.right_wheel_vel  = self.base_speed + 10
            self.left_wheel_vel = self.base_speed - 10


        self.motor_obj.set_velcoties(self.left_wheel_vel,self.right_wheel_vel )





def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = drive_rpi()

    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()




class setup(object):
    def __init__(self,mr_a,mr_b,mr_en,ml_a,ml_b,ml_en):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(mr_a, GPIO.OUT)
        GPIO.setup(mr_b, GPIO.OUT)
        GPIO.setup(mr_en,GPIO.OUT)

        GPIO.setup(ml_a, GPIO.OUT)
        GPIO.setup(ml_b, GPIO.OUT)
        GPIO.setup(ml_en,GPIO.OUT)

        GPIO.setmode(GPIO.BCM)
        GPIO.output(mr_a,1);
        GPIO.output(ml_a,1);
        self.mr_a=mr_a;self.mr_b=mr_b;
        self.ml_a=ml_a;self.ml_b=ml_b;
        self.mr_en=mr_en;self.ml_en=ml_en
        self.pwm_r =  GPIO.PWM(mr_en,1000)
        self.pwm_l =  GPIO.PWM(ml_en,1000)
        self.pwm_l.start(40)
        self.pwm_r.start(30)



    def stop(self):
        self.pwm_r.ChangeDutyCycle(0)
        self.pwm_l.ChangeDutyCycle(0)

    def set_velcoties(self,left_wheel_vel , right_wheel_vel ):
        print(left_wheel_vel," / ", right_wheel_vel )
        self.pwm_r.ChangeDutyCycle(right_wheel_vel )
        self.pwm_l.ChangeDutyCycle(left_wheel_vel)



    def motor_turn_off(self):
        GPIO.cleanup()
        sys.exit(0)


if __name__ == '__main__':
    main()