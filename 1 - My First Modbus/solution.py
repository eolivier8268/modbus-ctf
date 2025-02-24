from pymodbus.client import ModbusTcpClient

# connect to client
client = ModbusTcpClient("172.18.1.2", port=502)

# poll the first 32 registers
for i in range(32):
    response = client.read_holding_registers(i)
    print(response)

# we see registers 5 - 26 have data that appears to be ascii
flag = ""
for i in range(4,26):
    response = client.read_holding_registers(i)
    registerValue = response.registers[0]
    flag += chr(int(registerValue))
print(flag)