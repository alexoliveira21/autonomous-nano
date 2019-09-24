from adafruit_servokit import ServoKit

class Car():

    #creates and initializes a Car object
    def __init__(self, motorPin = 0, servoPin = 1, default_motor_angle = 90, default_servo_angle = 90, camera):

        self.motorPin = motorPin
        self.servoPin = servoPin
        self.default_motor_angle = default_motor_angle
        self.default_servo_angle = default_servo_angle
        self.camera = camera
        self.motor, self.servo = init_servos(self)

    # initializes motor and servo using the designated pins and default angles
    def init_servos(self):

        #initialize servos
        kit = ServoKit(channels = 16)
        motor = kit.servo[self.motorPin]
        servo = kit.servo[self.servoPin]

        #set default angles
        motor.angle = self.default_motor_angle
        servo.angle = self.default_servo_angle

        print("Motor set to pin {} with angle {}".format(self.motorPin, self.default_motor_angle))
        print("Servo set to pin {} with angle {}".format(self.servoPin, self.default_servo_angle))
        return motor, servo

    #changes throttle of car with given input
    def change_throttle(self, angle):

        self.motor.angle = angle

        print("Throttle changed to {}".format(angle))

    #changes steering angle to given angle
    def change_steering(self, angle):

        self.servo.angle = angle

        print("Steering angle changed to {}".format(angle))


    #performs an emergency stop on vehicle by setting it to its defaults
    def emergency_stop(self):
        self.motor.angle = self.default_motor_angle
        self.servo.angle = self.default_servo_angle
