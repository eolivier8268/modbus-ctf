import time
from random import randint
from pymodbus.client import ModbusTcpClient

# Server details
SERVER_IP = "172.18.7.2"  # Replace with actual server IP if needed
SERVER_PORT = 5020       # Port used by the server

# Create a Modbus TCP client instance
client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)

if client.connect():
    print("Connected to the Modbus server.")
    try:
        while True:
            value = randint(130, 150)
            # write a simulated temperature value to register 10
            result = client.write_register(10, value)
            if result.isError():
                print("Write error:", result)
            else:
                print(f"Sensor value written: {value}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Client stopped by user.")
    finally:
        client.close()
else:
    print("Failed to connect to the Modbus server.")
