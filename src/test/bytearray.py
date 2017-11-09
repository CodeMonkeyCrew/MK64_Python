from bitarray import bitarray as BitArray

curr_endian = 'big'

def setCommand(input, response):
    value = bin(int(input[0]))
    leng = 3 - (len(value)-2)

    for b in value[2:5]:
        response[leng] = int(b)
        leng += 1

    return response

def setValue(input, response, offset):
    value = int(input[1]/2)-1
    value = bin(value)
    leng = 10 -(len(value)-2)
    for b in value[2:10]:
        response[leng] = int(b)
        leng+=1
    return response

def createMessage(input):
    a = BitArray(10, endian=curr_endian)
    a.setall(False)
    a = setCommand(input, a)
    a = setValue(input, a, 3)
    return a

for x in range(0,8):
    input = [x, 256]
    #createMessage(input)
    print(createMessage(input).to01())


''' 
Returns
Command|Value  |
|000   |0000000|
'''