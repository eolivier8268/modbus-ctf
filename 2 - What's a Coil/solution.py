from pymodbus.client import ModbusTcpClient

# connect to client
client = ModbusTcpClient("127.0.0.1", port=5020)

# get device info
print(client.read_device_information())

# poll the first 100 coils
for i in range(100):
    response = client.read_coils(i)
    print(f"Coil {i}: {response.bits}")

# poll the first 100 registers
for i in range(100):
    response = client.read_holding_registers(i)
    print(f"Register {i}: {response.registers}")

# From here we see coil 5 is true, regs 3 and 22 have data
# also see a contiguous block starting at register 50 that could be text, 
# let's decode by adding the code below

message = ""
for i in range(50,78):
    response = client.read_holding_registers(i)
    registerValue = response.registers[0]
    message += chr(int(registerValue))
print(message)

# With the hint above, we can print the code
# Yes, we are doing some nasty type conversions to print the coil outputs, 
# but it should be obvious that true = 1 and false = 0 from the above
print("Coil 05: " + str(int(client.read_coils(5).bits[0])))
print("Coil 17: " + str(int(client.read_coils(17).bits[0])))
print("Reg  03: " + str(client.read_holding_registers(3).registers[0]))
print("Reg  22: " + str(client.read_holding_registers(22).registers[0]))