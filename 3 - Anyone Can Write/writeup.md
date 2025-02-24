# Challenge - Anyone can Write
You have gained access to a modbus device at 172.18.3.2. You found a spec sheet for the device stating that the integer on holding register 10 is used to control the device. Can you find a way to overwrite this register and unlock the flag?

Flag format: DELOGRAND{}

# Hints
Not sure what to overwrite the register with? How big is a modbus holding register?
https://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf (pg 6)

# Solution
See `solution.py` - the intended solution is to brute force the value in the specified register