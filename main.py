import input_controller
import zigbee

devices = input_controller.get_available_devices()
input_controller.start_listening(devices, zigbee.send_command)