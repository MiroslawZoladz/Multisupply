from pwm import Pwm

from time import sleep

pwm = Pwm()
pwm.enable()
sleep(2)
pwm.freq_set(30)
pwm.pwm_set(30)
# sleep(2)
pwm.disable()
pwm.save()




