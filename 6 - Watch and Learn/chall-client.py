import time
from random import randint
from pymodbus.client import ModbusTcpClient

# Server details
SERVER_IP = "172.18.6.2"    # Replace with actual server IP if needed
SERVER_PORT = 5020          # Port used by the server

# Create a Modbus TCP client instance
client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)

if client.connect():
    print("Connected to the Modbus server.")
    try:
        while True:
            # Write the sensor value (2500) to holding register at address 1 (0-based indexing)
            temp = randint(1995, 2005)
            result = client.write_register(10, temp)
            if result.isError():
                print("Write error:", result)
            else:
                print("Sensor value written: 2500")
            # Wait for 1 second before writing the next value
            time.sleep(1)
    except KeyboardInterrupt:
        print("Client stopped by user.")
    finally:
        client.close()
else:
    print("Failed to connect to the Modbus server.")
