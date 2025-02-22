from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore.store import ModbusSequentialDataBlock
import threading


# Set up the Modbus memory
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0] * 100),   # Discrete Inputs (Not used)
    co=ModbusSequentialDataBlock(0, [0] * 100),   # Coils (Not used)
    hr=ModbusSequentialDataBlock(0, [0] * 100),   # Holding Registers
    ir=ModbusSequentialDataBlock(0, [0] * 100)    # Input Registers (Not used)
)

# Store a hidden flag in registers (in ASCII format)
flag = "DELOGRAND{modbus_overwrite}"
flag_ascii = [ord(char) for char in flag]

# Hidden flag location: Registers 50-64 (Initially sanitized)
store.setValues(3, 50, [0] * len(flag_ascii))
store.setValues(3, 50, flag_ascii[0:10])
store.setValues(3, 76, [flag_ascii[26]])

# Define the secret values to unlock the flag
SECRET = 2026  # Address 10

# Function to monitor the registers and reveal the flag if correct
def unlock_flag(context):
    while True:
        try:
            # Read current values
            value = context[0].getValues(3, 10, count=1)[0]

            # If both values are correct, reveal the flag
            if value == SECRET:
                print("Correct value entered! Unlocking the flag...")
                context[0].setValues(3, 50, flag_ascii)
                break
        except Exception as e:
            print(f"Error monitoring registers: {e}")

# Launch the Modbus server
context = ModbusServerContext(slaves=store, single=True)

print("🚀 Modbus TCP Challenge is running on port 5020...")
monitor_thread = threading.Thread(target=unlock_flag, args=(context,))
monitor_thread.start()

# Start the server
StartTcpServer(context, address=("0.0.0.0", 5020))
