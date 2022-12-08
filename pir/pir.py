import RPi.GPIO as GPIO
import time

# Declare pin
pir = 7
led = 11
gpio_switch = 13

# Setup GPIO inputs and outputs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,GPIO.LOW)
GPIO.setup(gpio_switch,GPIO.IN)

try:
    while True:
        while GPIO.input(gpio_switch)==1:
            # the switch is in the "on" position
            if(GPIO.input(pir)):
                GPIO.output(led,GPIO.HIGH)
                print("Motion Detected!")
            else:
                GPIO.output(led,GPIO.LOW)
                print("No Motion Detected!")
            time.sleep(1)
        # turn off the LED
        GPIO.output(led,GPIO.LOW)

# Gracefully cleanup and free the GPIO when user terminates the program by pressing Ctrl-C
except KeyboardInterrupt:
    print("Stopping")
    GPIO.output(led,GPIO.LOW)
    GPIO.cleanup()