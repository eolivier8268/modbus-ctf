from pymodbus.client import *

client = ModbusTcpClient("127.0.0.1", port=502)
info = client.read_device_information()
print(info.information)