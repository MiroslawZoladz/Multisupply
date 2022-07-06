HELP =""" Commands

# supply
sch: set current channel
sv : set voltage as current electrical parameter
si : set current as current electrical parameter
sp : set voltage (0-63)
sea: enable all channels
sda: disable all channels
sech : enable current channel
sm : measure current param (U/I) at current channel

# suply service
sc : callibration in mili
sr : read register
sf : read coefficient
sg : [brng/pg/badc] config device

# v out
och  : set current channel
ov   : set voltage ( 2 args)
omin: set min
omax: set max (c.a. 1.2V)
oc  : calibrate, args: out0 min, out1 min, out0 max, out1 max,
od  : connect to gnd

# v in
ai : read analog input (diff n-p)
aic: callibrate, arg: applied diff n-p value

# hv
hve : enable
hvd : disable
hvs : save
"""

from machine import Pin, PWM, SoftI2C
from display import Display
from board import Board
from analog_outputs import AnalogOutputs
from analog_input   import AnalogInput
from HV import HV
from config_jumpers import JMP
from pwm import Pwm

# pwm = PWM(Pin(10))
# pwm.freq(10000)
# pwm.duty_u16(pow(2,16)//10)

sda=Pin(17)
scl=Pin(18)
i2c=SoftI2C(sda=sda, scl=scl, freq=400000)

disp = Display(i2c)

board = Board(i2c)
ao = AnalogOutputs()
ai = AnalogInput()
hv = HV(disable=True)
pwm = Pwm()



disp.show_str('remote\ncontrol')

while True:
    
    command = input("cmd?:")
    
    try:
        tokens = command.split()
        if not tokens:
            print(HELP)
            continue
        cmd, arg  = tokens[0], [float(s) for s in tokens[1:]]
        
        # supply
        if   cmd == 'sea': board.enable_all()
        elif cmd == 'sda': board.disable_all()
        elif cmd == 'sech' : board.enable_channel()
        elif cmd == 'sch': board.set_channel(int(arg[0]))
        elif cmd == 'sv' : board.set_param('v')
        elif cmd == 'si' : board.set_param('c')
        elif cmd == 'sp' : board.set(int(arg[0]))
        elif cmd == 'sm' :            
            val = board.measure()
            if val>10000:
                val  = 0
            print(val)
        elif cmd == 'sc': board.callib(int(tokens[1]))
        elif cmd == 'sg': board.config(arg[0], int(arg[1]))
        elif cmd == 'sf': print(board.coeff())
        elif cmd == 'sr': print(board.raw())
        
        # v out    
        elif cmd == 'od'  : ao.gnd()
        elif cmd == 'och' : ao.set_channel(int(arg[0]))
        elif cmd == 'ov'   : ao.set_voltage(float(arg[0]))
        elif cmd == 'omin': ao.min()
        elif cmd == 'omax': ao.max()
        elif cmd == 'oc'  : ao.callib(*arg)
        
        # v in
        elif cmd == 'iv' : print(f'{ai.get_voltage():0.4f}') 
        elif cmd == 'ic': ai.callib(*arg)
        
        # HV
        elif cmd == 'hve': hv.enable()
        elif cmd == 'hvd': hv.disable()
        
        # PWM
        elif cmd == 'pe': pwm.enable()
        elif cmd == 'pd': pwm.disable()
        elif cmd == 'pf': pwm.freq_set(int(arg[0]))
        elif cmd == 'pp': pwm.pwm_set(int(arg[0]))
        
        else: print(HELP)
        
        print('ok')

    except:
        print('Error')

