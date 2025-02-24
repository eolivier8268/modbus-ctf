# Challenge - What's this Device
Another device has been found on the network, at 172.18.4.2. Before attacking this device, we want to learn more about it. What is the device's product code?

Flag format: DELOGRAND{product code}

NOTE: the same device is used for challenge 5, so do not take it down when you are done.

# Solution 1 - nmap
The nmap modbus-discover script will query the device for information
```
nmap -p502 --script modbus-discover 172.18.4.2
```

# Solution 2 - pymodbus
```
from pymodbus.client import *

client = ModbusTcpClient("172.18.4.2", port=502)
response = client.read_device_information()
print(response.information)
```