import binascii
import struct

data = (1, 'ab'.encode('utf-8'), 2.7)
s = struct.Struct('I 2s f')
dataPack = s.pack(*data)
print(data)
print(s.format)
print(s.size)
print(binascii.hexlify(dataPack))
print(s.unpack(dataPack))