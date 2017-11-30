import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.bits_per_word = 8
spi.cshigh = False
spi.loop = False
spi.lsbfirst = False
spi.max_speed_hz = 9600
spi.mode = 0b00 # clock polarity 0, clock phase 0
gspi.threewire = False

def send_command_over_spi(message):
    try:
        resp = spi.xfer([(message[0] & 0xFF),message[1] & 0XFF])
        value = resp[0] & 0xFF
        while True:
            print("sending: ", value)
            resp = spi.xfer([value])
            value = resp[0] & 0xFF
            print("received: ", value)
            time.sleep(0.1)
        #end while
    except KeyboardInterrupt:
        spi.close()
    #end try 

