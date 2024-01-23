import gpiod
import time
import random

# Define the GPIO pins for the LEDs
LED_PINS = [2, 3, 4]

# Access the GPIO chip
chip = gpiod.Chip('gpiochip4')  # Assuming the LEDs are connected to the first GPIO chip

# Get the lines for each LED pin
led_lines = [chip.get_line(pin) for pin in LED_PINS]

# Request each line for output
for line in led_lines:
    line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        # Randomly select one LED
        selected_led = random.choice(led_lines)

        # Turn on the selected LED
        selected_led.set_value(1)
        time.sleep(0.1)

        # Turn off the selected LED
        selected_led.set_value(0)
        time.sleep(0.1)
finally:
    # Release all lines when done
    for line in led_lines:
        line.release()
