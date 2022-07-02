import sys
sys.path.append('../lib')
import machine
from board import Board

sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.SoftI2C(sda=sda, scl=scl, freq=100000)

My_board = Board(i2c)

# My_board.set_pot(4)
# My_board.set_meter(4, 'c')
# My_board.config('sadc', 0xF)
# My_board.config('badc', 0xF)
# My_board.config('brng', 0x0)
# My_board.config('pg', 0x0)
# My_board.config('md', 0x7)
print(My_board.measure())