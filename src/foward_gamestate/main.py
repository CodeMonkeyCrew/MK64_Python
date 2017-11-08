#start serial
import serial

import asyncio
import websockets

open_ser: serial

def open_serial_port(port, rate):
    global open_ser
    open_ser =  serial.Serial(port, baudrate=rate)

def readlineCR():
    rv = ""
    while True:
        ch = open_ser.read()
        rv += ch
        if ch == '\r' or ch == '':
            return rv

#receive data

# send data to registered
async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()