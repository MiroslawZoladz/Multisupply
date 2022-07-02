from machine import Pin
from mcp4021 import MCP4021
from ina219 import INA219_Voltage, INA219_Current

class channel:
    def __init__(self, pot, meters):
        self.pot = pot
        self.meters = meters
        
class Board:
    
    __MAX_CHANNEL_NR = 5
    
    __channel_cs_numbers = 27,26,22,21,20 
    __channel_addresses = 0x44, 0x43, 0x42, 0x41, 0x40
   
    __channel_en_numbers = 5, 6, 7, 8, 9
   
    def __init__(self, i2c):
        
        self.channels = []
        for channel_cs_nr, channel_addr in zip(self.__channel_cs_numbers, self.__channel_addresses):
            p = MCP4021(channel_cs_nr)
            m = {'c':INA219_Current(i2c, channel_addr), 'v':INA219_Voltage(i2c, channel_addr)}
            self.channels.append(channel(pot = p, meters = m))
        
        self._channel = 0
        self._param = 'v'
        self.current_pot = self.channels[self._channel].pot
        self.current_meter = self.channels[self._channel].meters[self._param]
        self.enable = [Pin(pin_nr,Pin.OUT, value = 0) for pin_nr in self.__channel_en_numbers]
    
    def enable_channel(self):        
        self.enable[self._channel].on()

    def disable_all_channels(self):        
        for e in self.enable: e.off()        

    def enable_all_channels(self):        
        for e in self.enable: e.on()        
    
    def set_channel(self, chan_nr):
        self._channel = chan_nr
        self.current_pot = self.channels[chan_nr].pot
        self.current_meter = self.channels[chan_nr].meters[self._param]
    def set_param(self, param):
        self._param = param
        self.current_meter = self.channels[self._channel].meters[param]        
    def set(self, value):
        self.current_pot.set(value)
    def inc(self):
        self.current_pot.inc(1)
    def dec(self):
        self.current_pot.dec(1)
    def save(self):
        for chan in self.channels:
            chan.pot.save()
    def measure(self):
        return self.current_meter.measure()
    def callib(self, value):
        self.current_meter.callib(value)
    def config(self, name, value):
        self.current_meter.config(name, value)
    def coeff(self):
        return self.current_meter.read_coefficient()
    def raw(self):
        return self.current_meter.measure_raw()
        