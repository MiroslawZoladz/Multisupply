import sys
sys.path.append('../lib')

from adc_mcp3464 import ADC
from board_pinout import BoardPinout

class AnalogInputs:
    CHANELL_NR = 12
    def __init__(self):
        bp = BoardPinout()
        self.adc = [ADC(bp.SPI_SCK, bp.SPI_MOSI, miso, cs) for miso, cs in zip((bp.SPI_MISO_ADC_0,bp.SPI_MISO_ADC_1),(bp.SPI_CS_ADC_0,bp.SPI_CS_ADC_1))]
        
    def voltages(self, ch_nr):
        assert ch_nr <= self.CHANELL_NR, 'ERR channel_nr_to_big' 
                
        if ch_nr <= 7:
            r0 = ch_nr
            r1 = 0
        else:
            r0 = 7
            r1 = ch_nr%7
            
        voltages = list()    
        for i in range(r0): # adc0 1-..
            voltages.append(self.adc[0].voltage(0,i+1))
        for i in range(r1): # adc1 1-..
            voltages.append(self.adc[1].voltage(0,i+1))
            
        return voltages
        
    def callib(self, v_at_adc_0_ch1, v_at_adc_1_ch1): #wzglêdem ch0
        self.adc[0].callib(v_at_adc_0_ch1)
        self.adc[1].callib(v_at_adc_1_ch1)


