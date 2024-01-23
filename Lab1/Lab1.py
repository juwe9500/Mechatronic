import RPi.GPIO as GPIO
import time

# Set up GPIO using Board numbering
GPIO.setmode(GPIO.BOARD)

# Set up pin 12 (GPIO 18) as an output
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)


# Turn on the GPIO pin
GPIO.output(3, GPIO.HIGH)
print("GPIO 2 is on.")

GPIO.output(5, GPIO.HIGH)
print("GPIO 3 is on.")

GPIO.output(7, GPIO.HIGH)
print("GPIO 4 is on.")

# Keep the pin on for 5 seconds
time.sleep(5)


# Turn off the GPIO pin and clean up
GPIO.output(3, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
GPIO.output(7, GPIO.LOW)
GPIO.cleanup()
