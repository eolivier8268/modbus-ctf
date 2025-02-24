import time
import sys
import threading
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore.store import ModbusSequentialDataBlock
from pymodbus.device import ModbusDeviceIdentification

# Global variables for tracking requests and flag state
REQUEST_THRESHOLD = 50  # Number of consecutive writes needed to trigger the vulnerability
RESET_INTERVAL = 10 # Time in seconds before the counter resets
request_counter = 0
lock = threading.Lock()

def reset_counter():
    """Resets the request counter after a fixed interval."""
    global request_counter
    with lock:
        request_counter = 0
    print("[DEBUG] Request counter reset.")
    threading.Timer(RESET_INTERVAL, reset_counter).start()  # Schedule next reset

class DoSDataBlock(ModbusSequentialDataBlock):
    def setValues(self, address, values):
        """
        Override the setValues method to monitor writes to register 10.
        When a write to register 10 occurs, we increment a counter.
        If the number of writes exceeds the threshold, the flag is released
        by writing its ASCII representation into registers starting at address 100.
        """
        global request_counter
        # Check if the write is specifically to register 10
        if address == 10:
            request_counter += 1
            print(f"[DEBUG] Write request #{request_counter} to register 10.")
            # If threshold reached and flag not yet released, release the flag.
            if request_counter >= REQUEST_THRESHOLD:
                print("[DEBUG] Request threshold reached. Triggering vulnerability...")
                sys.exit(1)
        super().setValues(address, values)

# Create a data store using our custom DoSDataBlock for holding registers.
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0] * 100),
    co=ModbusSequentialDataBlock(0, [0] * 100),
    hr=DoSDataBlock(0, [0] * 200),
    ir=ModbusSequentialDataBlock(0, [0] * 100)
)

context = ModbusServerContext(slaves=store, single=True)

def run_server():
    print("Starting DoS vulnerable Modbus server on port 5020...")
    threading.Timer(RESET_INTERVAL, reset_counter).start()  # Start reset timer
    StartTcpServer(context=context, address=("0.0.0.0", 5020))

if __name__ == "__main__":
    run_server()
