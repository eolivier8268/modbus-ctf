from pymodbus.client import *

client = ModbusTcpClient("172.18.4.2", port=502)
info = client.read_device_information()
print(info.information)