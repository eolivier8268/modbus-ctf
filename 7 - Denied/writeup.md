# Challenge - Denied
We've found another modbus device. After doing some research, our SCADA guy told us that it is vulnerable to a denial of service attack. Crash the device to get the flag. The device's control panel is at 172.18.7.4:8080

# Hint
What does normal operation look like for this device? Can you mimic "normal," but at an extremely high volume?

# Solution
Normal load for the server is that the client will write a new temperature every 5 seconds. You can see this through the control panel. You can then enumerate the device to determine that the corresponding register is 10. 

The server contains a condition where if it receives more than 50 requests in a 10 second interval, it will simply crash. A simple python script or automation of your favorite tool can be used to trigger this condition by continuously writing a value to register 10 to crash the server. 

See `solution.py` for a solution written in pymodbus. 