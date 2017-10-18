import input_controller, serial_controller, asyncio, config_reader


#Read Settings
config = config_reader.read_config('settings.ini')

#Init Controller
devices = []
for port in config['Controller']:
    input_port = config['Controller'][port]
    if input_port:
        devices.append(input_controller.init_input_device(config['Controller']['Controller1_Port']))
#Init Serial
#serial_controller.open_serial_port(config['Serial']['Serial_Port'],config['Serial']['Baudrate'])

#Start

event_loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
#event_loop.run_until_complete(serial_controller.receive_data())
event_loop.run_until_complete(input_controller.start_listening(devices, serial_controller.send_data))
event_loop.close()
