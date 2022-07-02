import sys
sys.path.append('../lib')

from adc_mcp3464 import ADC
from board_pinout import BoardPinout

bp = BoardPinout()

MISO_PN = bp.SPI_MISO_ADC_1
CS_PN   = bp.SPI_CS_ADC_1

adc = ADC(bp.SPI_SCK, bp.SPI_MOSI, MISO_PN, CS_PN)
adc.callib(1.2095)

while(1):
    _ = ' '.join([f'{adc.voltage(0,i):0.3f}'for i in range(8)])
    print(_)


