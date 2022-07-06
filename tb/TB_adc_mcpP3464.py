import sys
sys.path.append('../lib')

from adc_mcp3464 import ADC
from board_pinout import BoardPinout

bp = BoardPinout()

MISO_PN = bp.SPI_MISO_ADC_0
CS_PN   = bp.SPI_CS_ADC_0

adc = ADC(bp.SPI_SCK, bp.SPI_MOSI, MISO_PN, CS_PN)
adc.callib(1.2145)

while(1):
    print(f'{adc.voltage(0,4):0.3f}')


