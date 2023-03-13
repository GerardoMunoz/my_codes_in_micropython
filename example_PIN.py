from machine import Pin,Timer



# Define GP25 pin (LED of pico) in output mode 
pin_led = Pin(25, mode=Pin.OUT)

# Set a voltage of 3.3V at the output (high logic state)
pin_led.on()
pin_led.high()
pin_led.value(1)
pin_led(1)

# Set a voltage of 0V at the output (low logic state)
pin_led.off()
pin_led.low()
pin_led.value(0)
pin_led(0)


# Function to be used in timer callback
def toggle_led(t:Timer):
    pin_led(not pin_led())

# Set a timer to interrupt each 500ms and run the callback
Timer().init(mode=Timer.PERIODIC, period= 500, callback=toggle_led)

###########################################
# Define in GP0 (near to usb port in pico) in input mode 
pin_button = Pin(0, mode=Pin.IN, pull=Pin.PULL_UP)
# Use PULL_UP when the button is conected to 0V

# Read 0 if the input has 0v, or 1 if the input has 3.3V 
value_1 = pin_button.value()
value_2 = pin_button()
print (value_1, value_2) # both are equal

# Function to be used in timer callback
def print_button(t:Timer):
    print("print_button:",pin_button())

# Set timer's interrupt each 2500ms and run the callback
Timer().init(mode=Timer.PERIODIC, period = 2500, callback=print_button)
# Don´t set period=0ms

# Function to be used in timer callback
def print_FALLING(pin:Pin):
    print("FALLING",pin)

# Set interrupt when input FALLING and run the callback (i.e. handler)
pin_button.irq(trigger=Pin.IRQ_FALLING, handler=print_FALLING)

# For debonce use timer interrupt over 20ms




