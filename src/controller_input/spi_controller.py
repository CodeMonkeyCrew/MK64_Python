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
spi.threewire = False

def send_command_over_spi(message):
    try:
        print("send:", message)
        resp = spi.xfer([(message[0] & 0xFF),message[1] & 0XFF])
        print("received: ", resp)
        time.sleep(0.1)
        #end while
    except KeyboardInterrupt:
        spi.close()
    #end try 

