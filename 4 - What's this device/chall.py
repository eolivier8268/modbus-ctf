from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore.store import ModbusSequentialDataBlock
from pymodbus.device import ModbusDeviceIdentification

# Create a data store for your slave
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),
    co=ModbusSequentialDataBlock(0, [0]*100),
    hr=ModbusSequentialDataBlock(0, [0]*100),
    ir=ModbusSequentialDataBlock(0, [0]*100)
)

# Create a server context with a specific slave id if desired
context = ModbusServerContext(slaves={1: store}, single=False)

# Customize the device identification (the slave ID data identifier)
identity = ModbusDeviceIdentification()
identity.VendorName  = 'Schneider Electric Power Meter 710'
identity.ProductCode = 'PM710MG'
identity.VendorUrl   = 'https://www.se.com/'
identity.ProductName = 'Schneider Power Meter 710'
identity.ModelName   = ' PM710'
identity.MajorMinorRevision = '03.110'

print("Starting Modbus server on port 502...")
StartTcpServer(context, identity=identity, address=("0.0.0.0", 502))
