from machine import Pin
from board_pinout import BoardPinout

class JMP:
    def __init__(self):        
        self.pin_rmt_ctl = Pin(BoardPinout.JMP_RMT_CTL, Pin.IN,Pin.PULL_UP)
        self.pin_pow_on  = Pin(BoardPinout.JMP_POW_ON, Pin.IN,Pin.PULL_UP)
        self.rmt_ctl = (self.pin_rmt_ctl.value()==0)
        self.pow_on  = (self.pin_pow_on.value()==0)
        
    def  rmt_ctl(self):
        return self.rmt_ctl
    
    def  pow_on(self):
        return self.rmt_ctl


