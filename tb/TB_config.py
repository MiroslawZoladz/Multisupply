import sys
sys.path.append('../lib')
from config import Config

my_config = Config(['a', 'b', 'c', 'd'], [12, 8, 4, 0], [0xA, 0xB, 0xC, 0xD])

print(my_config.get_bytes())

my_config.set('a', 0xD)
my_config.set('b', 0xC)
my_config.set('c', 0xB)
my_config.set('d', 0xA)

print(my_config.get_bytes())