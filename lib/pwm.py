from machine import Pin,PWM
from board_pinout import BoardPinout
from nonvolatile import NonVolatile

class Pwm:
    def __init__(self):
        
        self.disable()
        
        self.freq = NonVolatile(default=10)    
        self.pwm = NonVolatile(default=50)
        
        self.freq_range = range(10,100)
        self.pwm_range = range(1,50)
    
    def enable(self):
        self.PWM = PWM(Pin(BoardPinout.PWM))
        self.freq_set(self.freq.get())
        self.pwm_set(self.pwm.get())
    
    def disable(self):
        self.PWM =Pin(BoardPinout.PWM, Pin.OUT, value=0)
        
    def save(self):
        self.freq.save()      
        self.pwm.save()
        
    def freq_set(self,f):
        assert self.freq_range.start <= f <= self.freq_range.stop, 'frequency out of range'
        self.freq.set(f) 
        self.PWM.freq(f*1000)
    
    def freq_get(self):
        return self.freq.get()
        
    def freq_inc(self):
        f = self.freq.get()
        max_ = self.freq_range.stop
        if f < max_: f += 1
        self.freq.set(f)
        self.freq_set(f)
        
    def freq_dec(self):
        f = self.freq.get()
        min_ = self.freq_range.start
        if f > min_: f -= 1
        self.freq.set(f)
        self.freq_set(f)
        
    def pwm_set(self,pwm):
        assert self.pwm_range.start <= pwm <= self.pwm_range.stop, 'pwm out of range'
        self.pwm.set(pwm)     
        self.PWM.duty_u16(int(pow(2,16)*(pwm/100)))
    
    def pwm_get(self):
        return self.pwm.get()
        
    def pwm_inc(self):
        pwm = self.pwm.get()
        max_ = self.pwm_range.stop
        if pwm < max_: pwm += 1
        self.pwm.set(pwm)
        self.pwm_set(pwm)
        
    def pwm_dec(self):
        pwm = self.pwm.get()
        min_ = self.pwm_range.start
        if pwm > min_: pwm -= 1
        self.pwm.set(pwm)
        self.pwm_set(pwm)




