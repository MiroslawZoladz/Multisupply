import sys
sys.path.append('../lib')

from analog_input import AnalogInput

ai = AnalogInput()
# ai.callib(1.213)
while(1):
    print(f'{ai.voltage():0.3f}')


