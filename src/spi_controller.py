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
def merge(a, b):
    return 256 * a + b

def send_receive_over_spi(player, message):
    try:
        print("send:", message)
        resp = spi.xfer([(message[0].value & 0xFF),message[1] & 0XFF, 0x00, 0x00])
        print("received: ", resp)
        if resp:
            tmp = 0
            for item in resp:
                tmp = merge(tmp, item)
            print(tmp)
            player.connection.send(str(tmp).encode())      
        #end while
    except KeyboardInterrupt:
        spi.close()
    #end try 

