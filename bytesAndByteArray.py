'''
bytes() and bytearray() function they are return byte value of a integer or array of
integer.
bytes: bytes is a represents of group of byte values.

'''
data=[1000]
# bytesData=bytes(data) #through error
# print(bytesData) # ValueError: bytes must be in range(0, 256)

dataInt=1000
bytesDataInt=bytes(dataInt)
# print(bytesDataInt) # b'\x00\x00\x00\more.....

