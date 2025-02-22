# Challenge - What's this Device
Another device has been found on the network, at x.x.x.x. Before attacking this device, we want to learn more about it. What is the device's product code?

Flag format: DELOGRAND{product code}

# Solution 1 - nmap
The nmap modbus-discover script will query the device for information
```
nmap -p502 --script modbus-discover 127.0.0.1
```

# Solution 2 - pymodbus
```
from pymodbus.client import *

client = ModbusTcpClient("127.0.0.1", port=502)
response = client.read_device_information()
print(response.information)
```