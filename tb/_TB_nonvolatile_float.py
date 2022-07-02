import sys
sys.path.append('../lib')
from nonvolatile_float import nonvolatile_float

my_float = nonvolatile_float()

print(my_float.get())

my_float.set(1.7)

print(my_float.get())

my_float.save()