import spidev
import time

#config spi
spi = spidev.SpiDev()
spi.open(0, 0)
spi.bits_per_word = 8
spi.cshigh = False
spi.loop = False
spi.lsbfirst = False
spi.max_speed_hz = 9600
spi.mode = 0b00 # clock polarity 0, clock phase 0
spi.threewire = False

#merge hex values received over spi
def merge_hex(target, value, offset):
    return value << (8*offset) | target

#reverse every received package to fix wrong order
def reverse_bits(byte):
    byte = ((byte & 0xF0) >> 4) | ((byte & 0x0F) << 4)
    byte = ((byte & 0xCC) >> 2) | ((byte & 0x33) << 2)
    byte = ((byte & 0xAA) >> 1) | ((byte & 0x55) << 1)
    return byte

#send command and reiceive data. forward the data over websocket
def send_receive_over_spi(player, message):
    try:
        print("send:", message)
        resp = spi.xfer([(message[0].value & 0xFF),message[1] & 0XFF, 0x00, 0x00])
        if resp:
            tmp = 0
            index = 0
            for item in resp:
                tmp = merge_hex(tmp, reverse_bits(item), index)
                index += 1
            result = str(tmp).encode()
            print(result)
            player.connection.send(result)   
        #end while
    except KeyboardInterrupt:
        spi.close()
    #end try 