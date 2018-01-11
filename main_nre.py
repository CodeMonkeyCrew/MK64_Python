from spi_controller import send_receive_over_spi
from n64_keymap import N64_KEYS

while True:
    send_receive_over_spi(1,[0xAB,0xAB])