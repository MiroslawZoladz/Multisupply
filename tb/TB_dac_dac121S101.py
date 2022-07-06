import sys
sys.path.append('../lib')

from dac_dac121S101 import DAC
from board_pinout import BoardPinout
from time import sleep

bp = BoardPinout()
dac = [DAC(bp.SPI_SCK, bp.SPI_MOSI, bp.SPI_MISO_ADC_0, cs) for cs in (bp.SPI_CS_DAC_0, bp.SPI_CS_DAC_1)]

dac[0].gnd()
dac[1].gnd()
sleep(1)
dac[0].raw(1500)
dac[1].raw(0)


# #normal
# dac[0].gnd()
# dac[1].gnd()
# 
# sleep(2)
# 
# dac[0].min()
# dac[1].min()
# 
# sleep(2)
# 
# dac[0].max()
# dac[1].min()
# 
# sleep(2)
# 
# dac[0].voltage(0.6)
# dac[1].voltage(1.2)

# callib


# dac.min()
# dac.max()

# dac[0].callib(min_in_V=0.003495, max_in_V=3.30650)
# dac[1].callib(min_in_V=0.00211, max_in_V=3.30534)

# dac[0].voltage(0.600)
# dac[1].voltage(1.200)

# dac[0].raw(1500)
# dac[1].raw(1500)
