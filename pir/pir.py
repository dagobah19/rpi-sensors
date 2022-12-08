import RPi.GPIO as GPIO
import time

# Declare pin
pir = 7

# Setup GPIO inputs and outputs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir,GPIO.IN)

try:
    while True:
        if(GPIO.input(pir)):
            print("Motion Detected!")
        else:
            print("No Motion Detected!")
        time.sleep(1)

# Gracefully cleanup and free the GPIO when user terminates the program by pressing Ctrl-C
except KeyboardInterrupt:
    print("Stopping")
    GPIO.cleanup()