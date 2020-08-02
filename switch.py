import time
from grove.gpio import GPIO

__all__ = ['GroveLed', 'GPIO']

class Switch(GPIO):
    '''
    Class for Grove - XXXX Led

    Args:
        pin(int): number of digital pin the led connected.
    '''
    state = 0
    
    def __init__(self, pin):
        super(Switch, self).__init__(pin, GPIO.OUT)
        self.set_state(0)
        
    def set_state(self, state):
        self.write(state)
        self.state = state
        
    def get_state(self):
		return self.state
