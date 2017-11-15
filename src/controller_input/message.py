from bitarray import bitarray as BitArray

curr_endian = 'big'

def setCommand(input, response):
    value = bin(int(input))
    leng = 3 -(len(value)-2)
    for b in value[2:5]:
        response[leng] = int(b)
        leng += 1
    return response

def setValue(value, response):
    if(value == 0):
        value = 2
    value = int((value/2))-1
    value = bin(value)
    leng = 10 -(len(value)-2)
    for b in value[2:10]:
        response[leng] = int(b)
        leng+=1
    return response

def createMessage(input, value):
    message = BitArray(10, endian=curr_endian)
    message.setall(False)
    message = setCommand(input, message)
    message = setValue(value, message)
    return message


