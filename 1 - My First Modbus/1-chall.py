from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock

# Define Holding Registers (40001-40010)
data_block = ModbusSequentialDataBlock(0, [0] * 10)

# Store the flag in register 5 (40006)
flag_value = [ord(c) for c in "delogrand{R34D_2_ENUM}"]
data_block.setValues(5, flag_value)

# Create Modbus Memory Store
store = ModbusSlaveContext(hr=data_block)
context = ModbusServerContext(slaves=store, single=True)

# Start TCP Server on Port 5020
print("Starting Modbus server on port 502...")
StartTcpServer(context, address=("0.0.0.0", 502))
