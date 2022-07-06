import sys
sys.path.append('../lib')

from adc_mcp3464 import ADC
from board_pinout import BoardPinout
# from nonvolatile_float import nonvolatile_float
from nonvolatile import NonVolatile


class AnalogInput:
    def __init__(self):
        bp = BoardPinout()
        self.adc = ADC(bp.SPI_SCK, bp.SPI_MOSI, bp.SPI_MISO_ADC_0, bp.SPI_CS_ADC_0)
        self.volts_per_lsb = NonVolatile() 
        
    def get_voltage(self):            
        assert self.volts_per_lsb.get() != None, 'ERR adc_not_calibrated'           
        return self.adc.raw(0,4) * self.volts_per_lsb.get()      
        
    def callib(self, v_between_adc_ch0_4):
        lsb = self.adc.raw(0,4) #!!!
        self.volts_per_lsb.set(v_between_adc_ch0_4/lsb)
        self.volts_per_lsb.save()



