a=10
print(id(a))
print(hex(a))

from ctypes import c_int, addressof

b = c_int(22)
print(addressof(b))

d=44
print(d)

del d
print(d) #Error