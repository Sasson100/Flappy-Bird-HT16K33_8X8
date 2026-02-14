import time
from machine import Pin

class Button:
    def __init__(self, pin_num: int, debounce_ms = 30):
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        self.debounce_ms = debounce_ms

        self._state = not self.pin.value()
        self._last_change = time.ticks_ms()

        self._pressed_event = False
        self._released_event = False

        self.pin.irq(
            trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
            handler=self._irq_handler
        )


    def _irq_handler(self, pin: Pin):
        now = time.ticks_ms()
        new_state = not pin.value()

        # Ignore if still in debounce window
        if time.ticks_diff(now, self._last_change) < self.debounce_ms:
            return

        if new_state != self._state:
            self._state = new_state
            self._last_change = now

            if self._state:
                self._pressed_event = True
            else:
                self._released_event = True

    def is_pressed(self):
        return self._state

    def was_pressed(self):
        if self._pressed_event:
            self._pressed_event = False
            return True
        return False

    def was_released(self):
        if self._released_event:
            self._released_event = False
            return True
        return False
    
    def held_time(self,in_ms=True):
        if not self.is_pressed():
            return 0
        
        div = 1 if in_ms else 1000
        return time.ticks_diff(time.ticks_ms(),self._last_change)/div