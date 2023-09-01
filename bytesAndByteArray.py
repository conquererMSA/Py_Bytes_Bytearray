'''
bytes() and bytearray() function they are return byte value of a integer or array of
integer.
bytes: bytes is a represents of group of byte values.
8 bit equal 1 byte.
1 byte er sorbuccho represent hocce 256: max 1 byte(11111111)=255

print(bytes(3))=>b'\x00\x00\x00': ekhane null er bytes represnts hobe 3 times.
print(bytes(5))=>b'\x00\x00\x00\x00\x00': ekhane null er bytes represnts hobe 5 times.
print(bytes(0))=>b'': ekhane null er bytes represnts hobe 0 times ba kuno bytes
represenation nei.

print(bytes([31]))=>b'\x1f': ekhane 31 bytes representation hocce 1 times.
print(bytes([3,4,5,31]))=>b'\x03\x04\x05\x1f': ekhane eksathe 3,4,, and 5 er bytes
represnts hobe 1 times kore.
'''
data=[1000]
# bytesData=bytes(data) #through error
# print(bytesData) # ValueError: bytes must be in range(0, 256)

dataInt=1000
bytesDataInt=bytes(dataInt)
# print(bytesDataInt) # b'\x00\x00\x00\more.....
# print(bytes(0)) # b'' ekhane null er bytes represents hocce 0 times
# print(bytes(5)) # b'\x00\x00\x00\x00\x00 ekhane null'er bytes represents hocce 5 times
arrData=[31,4,5]
arrDataBytes=bytes(arrData)
# print(arrDataBytes) #b'\x1f\x04\x05'
print(bytes([31]))
