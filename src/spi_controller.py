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
        resp = spi.xfer([(message[0].value & 0xFF), message[1] & 0XFF, 0x00, 0x00])
        if resp:
            hex_result = 0
            offset = 0
            for package in resp:
                hex_result = merge_hex(hex_result, reverse_bits(package), offset)
                offset += 1
            player.connection.send(str(hex_result).encode())
            time.sleep(0.1)   
    except KeyboardInterrupt:
        spi.close()

