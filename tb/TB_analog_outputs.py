import sys
sys.path.append('../lib')

from analog_outputs import AnalogOutputs

ao = AnalogOutputs()
ao.min()
# ao.max()

# ao.callib(v0_min=0.00224, v1_min=0.00247, v0_max=1.21445, v1_max=1.21286)
# ao.voltage(0.123, 0.321)



