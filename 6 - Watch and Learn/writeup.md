# Challenge
During our web pentest we found a control panel for a modbus device at http://172.18.6.4:8080. Can you cause the device to overheat and get the flag?

# Hint
The flag will be read from the web control panel of the device, once unlocked

# Solution
You need to determine which register is being written to. You can either capture traffic and reverse the packet being sent by the client to confirm that it is register 10. Or you can view the registers on the device to see that the value in register 10 always corresponds with the web console.

Once you've determined this, any method of overwritting to the register will work. See `solution.py`.