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
# print(bytes([31]))

#looping on bytes
b=bytes([13,44,64])
# print(b) # b'\r,@'
# for bValue in b:
#   print(bValue) #13,34,67
# del b
# print(b) # NameError: name 'b' is not defined

arrData2=[23,56,78]
# print(arrData2[0:2]) # [23, 56]
b2=bytes(arrData2)
# print(b2[1]) #56
# print(b2[0:2]) #b'\x178' bytes representation for sequence of [23,56]
for byteItem in b2[0:2]:
    pass
    # print(byteItem) # 20 30

# print(b2[1:2]) # b'8'

# started bytearray
dt=[43,78,34]
dtBytes=bytes(dt)
# print(dtBytes) # b'+N"'
dtByteArray=bytearray(dt)
# print(dtByteArray) # bytearray(b'+N"')
#bytes() and bytearray() same result return kore.

char=97
# print(bytes([char]))
# print(chr(char))
# chr(unicode/ascii)=>charecter, bytes([unicode, ascii])=>b'charecter'
# bytes([char]) and chr(char) function same result return kore. Tobe ekti
# unicode/ascii value diye chr(97) ekti charecter pawya zay.
# Kintu bytes([97,98,99]) function diye eksathe onek gulu charecter byte
# representation e pawya zay. b'abc' for bytes([97,98,99])

charList=[65,97,100,112]
charBytes=bytes(charList)
# print(charBytes) # b'Aadp'
for byteChar in charBytes:
    pass
    # print(bytes([byteChar])) # b'A' b'a' b'd' b'p'
charHalf=charBytes[1:3]
# print(charHalf) # b'ad'
charListBytearray=bytearray(charList)
# print(charListBytearray) # bytearray(b'Aadp') same as bytes() function

#convert string to byte
name='MSA'
byteName=bytes(name,encoding='utf-8')
print(byteName) # b'MSA'
byteArrName=bytearray(name,encoding='utf-8')
# print(byteArrName) # bytearray(b'MSA')
# byteName[0]='N' # TypeError: 'bytes' object does not support item assignment

# bytearray is a mutable data type: assignment and modification are acceptable
# byteArrName[0]=b'G' # TypeError: 'bytes' object cannot be interpreted as an integer
byteArrName[0]=71
# print(byteArrName) # bytearray(b'GSA')
# bytearray te indexing diye kuno charecter modify korte hole assignment e unicode
# othoba ascii value dite hobe.
# like byteArrName[index]=charUnicode/ASCIIValue

# bytearray te list er sob method apply kora zay:
char2=[65,66,67,68]
char2Byte=bytearray(char2)
bIndex=char2Byte.index(b'B')
# print(bIndex) # 1
char2Byte.append(97)
# print(char2Byte) # bytearray(b'ABCDa')




