import sys
sys.path.append('../lib')
from machine import SoftI2C
from ina219 import INA219_Current,INA219_Voltage

sda=machine.Pin(17)
scl=machine.Pin(18)
i2c=SoftI2C(sda=sda, scl=scl, freq=100000)

# devices = i2c.scan()
# if len(devices) == 0:
#   print("No i2c device !")
# else:
#   print('i2c devices found:',len(devices))
#  
#   for device in devices:  
#     print("Decimal address: ",device," | Hexa address: ",hex(device))


# ina_cur = INA219_Current(i2c, 0x40)
ina = [INA219_Current(i2c, addr) for addr in (0x44, 0x43, 0x42, 0x41, 0x40)]

for i in ina:
    print(i.measure_raw(),end=' ')


# 
# print("Shunt voltage: %i " % ina_cur.measure())
# 
# # print("Bus voltage raw: %i " % ina_vol.measure_raw())
# # print("Shunt voltage raw: %i " % ina_cur.measure_raw())

# # ina_vol.config('sadc', 0xF)
# ina_cur.config('sadc', 0xF)
# 
# # ina_vol.config('badc', 0xF)
# ina_cur.config('badc', 0xF)
# 
# # ina_vol.config('pg', 0x0)
# ina_cur.config('pg', 0x0)
# 
# # ina_vol.config('brng', 0x0)
# ina_cur.config('brng', 0x0)
# 
# # print("Bus voltage raw: %i " % ina_vol.measure_raw())
# print("Shunt voltage raw: %i " % ina_cur.measure_raw())
# 
# # print("Bus voltage: %i " % ina_vol.measure())
# print("Shunt voltage: %i " % ina_cur.measure())
# 
# print("Coefficient: %f" % ina_cur.read_coefficient())
# 
# # ina_vol.callib(2)
# ina_cur.callib(32)
# 
# # print("%f" % ina_vol.read_coefficient())
# print("Coefficient: %f" % ina_cur.read_coefficient())

# print("Bus voltage: %i " % ina_vol.measure())
# print("Shunt voltage: %i " % ina_cur.measure())