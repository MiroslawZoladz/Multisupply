import sys
sys.path.append('../lib')

from analog_inputs import AnalogInputs

ai = AnalogInputs()
# ai.callib(1.21297, 1.20964)
while(1):
    _ = ' '.join([f'{v:0.3f}'for v in ai.voltages(7+5)]) 
    print(_)


