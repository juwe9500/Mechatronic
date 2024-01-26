import gpiod
import time

def control_led(led_number, state):
    # Define the GPIO pins for the LEDs
    LED_PINS = [2, 3, 4]

    # Access the GPIO chip
    chip = gpiod.Chip('gpiochip4')  

    # Get the lines for each LED pin
    led_lines = [chip.get_line(pin) for pin in LED_PINS]

    # Request each line for output
    for line in led_lines:
        line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

    try:
        if led_number == -1:
            # Control all LEDs
            for line in led_lines:
                line.set_value(state)
        else:
            # Control specific LED
            led_lines[led_number].set_value(state)
    finally:
        # Release all lines when done
        for line in led_lines:
            line.release()

# Example usage
control_led(1, 1)  # Turn on LED 1
time.sleep(1)
control_led(0, 1)  # Turn on LED 0
time.sleep(1)
control_led(-1, 1) # Turn on all LEDs
time.sleep(1)
control_led(-1, 0) # Turn off all LEDs
