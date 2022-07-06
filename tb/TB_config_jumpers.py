from config_jumpers import JMP
from machine import Pin, SoftI2C
from display import Display

sda=Pin(17)
scl=Pin(18)
i2c=SoftI2C(sda=sda, scl=scl, freq=400000)

disp = Display(i2c)

jmp = JMP()
rmt_ctl = jmp.rmt_ctl()
pow_on  = jmp.pow_on()

disp.show_str(f'R:{rmt_ctl}\nP:{pow_on}')



