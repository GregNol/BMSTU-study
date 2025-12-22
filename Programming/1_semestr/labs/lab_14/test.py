import struct

a = struct.pack('ii4s', 0, 1, b'abcd')
print(a)
print(struct.unpack('ii4s', a))
print(struct.calcsize('ii4s'))
print(type(b'abcd'))
print(b'abcd'.decode('utf-8'))
