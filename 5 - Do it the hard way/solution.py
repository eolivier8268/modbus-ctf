import socket
import struct

# MBAP packet header: needs an ID, protocol, length, and unit ID
# See page 5 of the modbus TCP/IP specification
transaction_id = 0x1337 # set by client; could be any number
protocol_id = 0x0000 # always 0
length = 0x0005 # length of the remainder of the packet - we have 5 more 1-byte vars to include
unit_id = 0x01 # id of the slave on multi-device network
# from pg 43 of the modbus specification - implementation of the read_device function
function_code = 0x2B
mei_type = 0x0E
read_device_id_code = 0x01
object_id = 0x01

# Pack the header and the payload together:
packet = struct.pack('>HHHBBBBB', transaction_id, protocol_id, length, unit_id, function_code, mei_type, read_device_id_code, object_id)

# Create a socket connection to the Modbus server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("172.18.4.2", 502))
    s.sendall(packet)
    response = s.recv(1024)

print(response)