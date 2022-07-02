import sys
sys.path.append('../lib')

from analog_outputs import AnalogOutputs

ao = AnalogOutputs()
# ao.min()
# ao.max()

# ao.callib(v0_min=0.00227, v1_min=0.00254, v0_max=1.2145, v1_max=1.213)
ao.voltage(0.5, 0.5)



