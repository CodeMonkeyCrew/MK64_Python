import spidev
import time
import pickle

spi = spidev.SpiDev()
spi.open(0, 0)
spi.bits_per_word = 8
spi.cshigh = False
spi.loop = False
spi.lsbfirst = False
spi.max_speed_hz = 9600
spi.mode = 0b00 # clock polarity 0, clock phase 0
spi.threewire = False
#send data to server over spi and recieve the gamestat
#the gamestate is forwerded to the connected clients
def merge(a, b, index):
    return b << (8*index) | a

def reverse_bits(byte):
    byte = ((byte & 0xF0) >> 4) | ((byte & 0x0F) << 4)
    byte = ((byte & 0xCC) >> 2) | ((byte & 0x33) << 2)
    byte = ((byte & 0xAA) >> 1) | ((byte & 0x55) << 1)
    return byte

def send_receive_over_spi(player, message):
    try:
        print("send:", message)
        resp = spi.xfer([(message[0].value & 0xFF),message[1] & 0XFF, 0x00, 0x00])
        if resp:
            tmp = 0
            index = 0
            for item in resp:
                tmp = merge(tmp, reverse_bits(item), index)
                index += 1
            result = str(tmp).encode()
            print(result)
            player.connection.send(result)   
        #end while
    except KeyboardInterrupt:
        spi.close()
    #end try 

