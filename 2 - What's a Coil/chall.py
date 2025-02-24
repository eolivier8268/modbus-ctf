from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore.store import ModbusSequentialDataBlock

# Initialize non-contiguous Modbus data storage
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0] * 100),   # Discrete Inputs (Not Used)
    co=ModbusSequentialDataBlock(0, [0] * 100),   # Coils (Discrete Outputs)
    hr=ModbusSequentialDataBlock(0, [0] * 100),   # Holding Registers
    ir=ModbusSequentialDataBlock(0, [0] * 100)    # Input Registers (Not Used)
)

# Set the challenge-specific values
store.setValues(1, 5, [1])   # Coil at address 5 → 1
store.setValues(1, 17, [0])  # Coil at address 17 → 0

store.setValues(3, 3, [7])   # Holding Register at address 3 → 7
store.setValues(3, 22, [3])  # Holding Register at address 22 → 3
hint = [ord(c) for c in "code=coil5+coil17+reg3+reg22"]
store.setValues(3, 50, hint)


# Wrap in server context
context = ModbusServerContext(slaves=store, single=True)

# Start Modbus TCP server on port 5020
print("🚀 Starting Modbus server on port 5020...")
StartTcpServer(context, address=("0.0.0.0", 5020))
