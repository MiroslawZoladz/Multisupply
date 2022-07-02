import sys
sys.path.append('../lib')

from dac_dac121S101 import DAC
from board_pinout import BoardPinout

class AnalogOutputs:
    def __init__(self):        
        bp = BoardPinout()
        self.dac = [DAC(bp.SPI_SCK, bp.SPI_MOSI, bp.SPI_MISO_ADC_0, cs) for cs in (bp.SPI_CS_DAC_0, bp.SPI_CS_DAC_1)]
        self.gnd()
        
    def voltage(self,v0,v1):
        for dac,v in zip(self.dac,[v0,v1]):
            dac.voltage(v)
            
    def gnd(self):
        for dac in self.dac:
            dac.gnd()
            
    def min(self):
        for dac in self.dac:
            dac.min()

    def max(self):
        for dac in self.dac:
            dac.max()
            
    def callib(self,v0_min, v1_min, v0_max, v1_max):
        self.dac[0].callib(min_in_V=v0_min, max_in_V=v0_max)
        self.dac[1].callib(min_in_V=v1_min, max_in_V=v1_max)
        
        
