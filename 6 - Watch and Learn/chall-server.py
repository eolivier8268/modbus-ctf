import time
import threading
from random import randint
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore.store import ModbusSequentialDataBlock

# Define the hidden flag and convert it to a list of ASCII values.
FLAG = "DELOGRAND{quietly_listen}"
flag_ascii = [ord(c) for c in FLAG]

# Create a datastore for the Modbus slave.
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0] * 100),   # Discrete Inputs (not used)
    co=ModbusSequentialDataBlock(0, [0] * 100),   # Coils (not used)
    hr=ModbusSequentialDataBlock(0, [0] * 100),   # Holding Registers
    ir=ModbusSequentialDataBlock(0, [0] * 100)    # Input Registers (not used)
)

# initialize sensor bank to approximately 2500
for i in range(30):
    store.setValues(3, i, [randint(1995, 2005)])

# Create a server context.
context = ModbusServerContext(slaves=store, single=True)

def monitor_sensor(ctx):
    """Monitor the sensor reading and unlock the flag when triggered."""
    while True:
        try:
            # Read the sensor value from holding register 1.
            sensor_value = ctx[0].getValues(3, 10, count=1)[0]
            if sensor_value > 9999:
                print("Sensor trigger detected! Unlocking flag...")
                # Write the flag (as ASCII values) to holding registers starting at address 50.
                ctx[0].setValues(3, 50, flag_ascii)
                break
        except Exception as e:
            print("Error reading sensor register:", e)
        time.sleep(1)

# Start a background thread to monitor the sensor value.
monitor_thread = threading.Thread(target=monitor_sensor, args=(context,))
monitor_thread.daemon = True
monitor_thread.start()

print("Starting Modbus server on port 5020...")
StartTcpServer(context=context, address=("0.0.0.0", 5020))