# Challenge - Do it the hard way
You've probably been using scripts or python libraries to query these modbusses. Now, it's time to look under the hood. Once you've solved challenge 4, use the modbus specification to craft a packet that can once again query the device for information. 

Modbus Protocol Specification: https://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf
Modbus TCP/IP Specification: https://www.modbus.org/docs/Modbus_Messaging_Implementation_Guide_V1_0b.pdf 

You should craft your packet and send it to the device to learn how to work with packets and byte-level data. Once your packet is able to query the server, submit it as a flag with each field in hex separated by underscores.
Flag Format: DELOGRAND{xxxx_xxxx_xxxx_xx_xx_xx_xx_xx}

*If you have a working solution and CTFd won't accept your flag, let me know.*

# Hint
Implement this in python with the `socket` and `struct` libraries

# Hint
Think you're crafting your packets correctly but not getting a responce from the device? What endianness does modbus use?

# Solution
Start with the Modbus TCP/IP implementation. Page 4 of this document outlines that Modbus TCP/IP packets require a packet to begin with a Modbus Application Protocol (MBAP) header
Page 5 describes the 4 fields in the header:
a 2-byte transaction ID, which can be set to anything by the client
a 2-byte protocol ID which is always just 0
a 2-byte length value which is the length of the remainder of the packet. 
a 1-byte unit identifier, which identifies a slave if multiple are on the same line. In this challenge, the slave sets this value to one, and the master has to match it. Since it is only 1 byte, you can brute force this value. 

The modbus protocol specification describes the individual "function codes" that can be sent to a slave to interact with it. You will need to use the "Read Device Identification" Function (0x2B) described on page 43. The request has the following fields
- a 1-byte function code: 0x2B
- a 1-byte MEI Type: 0x0E
    - (most functions omit this, but you can think about it as a sub-function code that distinguished between multiple functions with code 0x2B)
- a 1-byte Read Device ID Code: 0x01
    - Valid values are 0-4. Defines which ID categories to read: Baic, regular, reserved, or extended. ProductCode is in the basic category
- a 1-byte object ID code: 0x01
    - Describes the which field object to read

So, you can pack these values into a struct (make sure to specify Big Endian), then send them on the wire. See the solution.py for what this would look like. Your flag should be:
DELOGRAND{xxxx_0000_0005_01_2B_0E_01_01}
**Note 1:** regex should allow any 4-digit integer in the first field
**Note 2:** there are other ways to craft the packet and get the productCode field. This is the most direct way and references the ProductCode field, as opposed to reading from multiple fields. As the intent of the exercise is to craft the packet, I consider this the most correct solution I guess. 