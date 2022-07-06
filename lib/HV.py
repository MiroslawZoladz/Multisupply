from machine import Pin
from board_pinout import BoardPinout
from nonvolatile import NonVolatile

class HV:
    def __init__(self,disable=False):        
        self.pin = Pin(BoardPinout.HV_ENABLE, Pin.OUT, value=0)
        
        self.state = NonVolatile()
        
        if not disable:
            if  self.state.get():
                self.pin.on()
            else:
                self.pin.off()

    def  get_state(self):        
        return self.state.get()

    def  enable(self):
        self.pin.on()
        self.state.set(True)
    
    def  disable(self):
        self.pin.off()
        self.state.set(False)
        
    def  change(self):
        self.state.set(not self.state.get())
        self.pin.off()
               
        
    def save(self):
        self.state.save()        

    
