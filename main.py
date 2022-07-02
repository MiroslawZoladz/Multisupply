HELP ="""
#MAIN

#supply
ch: set current channel
v : set voltage as current electrical parameter
c : set current as current electrical parameter
s : set voltage (0-63)
ea: enable all channels
da: disable all channels
e : enable current channel
m : measure current param (U/I) at current channel

#biasing
ag : analog outputs at gnd
ao : set out0,1; 2 args in volts (floating points) 

#SERVICE
l : callibration in mili
a : archive settings 
r : read register
f : read coefficient
g : [brng/pg/badc] config device
"""

from machine import Pin, PWM, SoftI2C
from display import Display
from board import Board
from analog_outputs import AnalogOutputs
from analog_inputs import AnalogInputs

# pwm = PWM(Pin(10))
# pwm.freq(10000)
# pwm.duty_u16(pow(2,16)//10)

sda=Pin(17)
scl=Pin(18)
i2c=SoftI2C(sda=sda, scl=scl, freq=400000)

board = Board(i2c)
ao = AnalogOutputs()
disp = Display(i2c)

disp.show_str('remote\ncontrol')

while True:
    
    command = input("cmd?:")
    
    tokens = command.split()
    if not tokens:
        print(HELP)
        continue
    cmd, arg  = tokens[0], [float(s) for s in tokens[1:]]
    
    # supply
    if   cmd == 'ea': board.enable_all_channels()
    elif cmd == 'da': board.disable_all_channels()
    elif cmd == 'e' : board.enable_channel()
    elif cmd == 'ch': board.set_channel(int(arg[0]))
    elif cmd == 'v' : board.set_param('v')
    elif cmd == 'c' : board.set_param('c')
    elif cmd == 's' : board.set(int(arg[0]))
    elif cmd == 'm' :            
        val = board.measure()
        if val>10000:
            val  = 0
        print(val)
    elif cmd == 'l': board.callib(int(tokens[1]))
    elif cmd == 'g': board.config(arg[0], int(arg[1]))
    elif cmd == 'f': print(board.coeff())
    elif cmd == 'r': print(board.raw())
    elif cmd == 'a': board.save()
    
    # biasing    
    elif cmd == 'ag' : ao.gnd()
    elif cmd == 'ao' : ao.voltage(float(arg[0]),float(arg[1]))
    elif cmd == 'aomin' : ao.min()
    elif cmd == 'aomax' : ao.max()
    elif cmd == 'aoc': ao.callib(*arg)
    
    else: print(HELP)
