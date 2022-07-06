from machine import Pin, PWM, SoftI2C
from board import Board
from keyboard import keyboard
from display import Display
from analog_outputs import AnalogOutputs
from analog_input   import AnalogInput
from HV import HV
from config_jumpers import JMP
from pwm import Pwm

sda=Pin(17)
scl=Pin(18)
i2c=SoftI2C(sda=sda, scl=scl, freq=400000)

display = Display(i2c)
board = Board(i2c)
ao = AnalogOutputs()
ai = AnalogInput()
hv = HV()
pwm = Pwm()

board.enable_all()
ao.enable()
pwm.enable()

keyboard = keyboard()
channel = 0

menu = 'supp_ch0','supp_ch1','supp_ch2','supp_ch3','supp_ch4','HV','call_n','call_p','v_in','pwm_f','pwm_p'
item_ix = 0
menu_item_change = True
while True:
    key = keyboard.read()
    
    if   key == 'DOWN':
        item_ix -= int(item_ix > 0)
        menu_item_change = True
        
    elif key == 'UP'  :
        item_ix += int (item_ix < (len(menu)-1))
        menu_item_change = True
        
    elif key == 'LEFT':
        if 'supp' in item:
            board.dec()
        elif 'call' in item:
            ao.dec()
        elif 'HV' in item:
            hv.disable()
        elif 'pwm_f' in item:
            pwm.freq_dec()
        elif 'pwm_p' in item:
            pwm.pwm_dec()
            
    elif key == 'RIGHT':
        if   'supp' in item:
            board.inc()
        elif 'call' in item:
            ao.inc()
        elif 'HV' in item:
            hv.enable()
        elif 'pwm_f' in item:
            pwm.freq_inc()
        elif 'pwm_p' in item:
            pwm.pwm_inc()

    elif key == 'MIDDLE':
        board.save()
        ao.save()
        hv.save()
        pwm.save()

    # on menu item change 
    if menu_item_change:
        item = menu[item_ix]
        if 'supp' in item:
            channel = int(item[7])
            board.set_channel(channel)
        elif 'call' in item:
            ao.set_channel(1 if 'p' in item else 0)            
    
    # display    
    if 'supp' in item:       
        board.set_param('v')
        voltage = board.measure()
        board.set_param('c')
        current = board.measure()
        if current > 10000:
            current = 0        
        display.show_supply(channel, voltage/1000, current/1000)
    elif 'call' in item:
        display.show_voltage(ao.get_name(), ao.get_voltage())
    elif 'v_in' in item:
        display.show_voltage('Vin', ai.get_voltage())
    elif 'HV' in item:
        s = 'ON' if hv.get_state() else 'OFF'
        display.show_str(f'HV: {s}')
    elif 'pwm_f' in item:        
        display.show_str(f'strobe\nfreq: {pwm.freq.get()}k')
    elif 'pwm_p' in item:        
        display.show_str(f'strobe\npwm: {pwm.pwm.get()}%')  
            

