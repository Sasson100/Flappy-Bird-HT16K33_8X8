from machine import Pin
import time

button = Pin(23, Pin.IN, Pin.PULL_UP)

button_pressed = False
last_value_change = time.ticks_ms()

def button_isr(pin: Pin):
    global button_pressed, last_value_change
    
    now = time.ticks_ms()
    if time.ticks_diff(now, last_value_change)>30:
        button_pressed = not pin.value()
        last_value_change = now

button.irq(trigger = Pin.IRQ_RISING | Pin.IRQ_FALLING, handler = button_isr)

while True:
    if button_pressed:
        button_pressed = False
        print("Button pressed")