# Challenge - What's a Coil
You have gained access to another modbus device at 172.18.2.2. However, critical operational data is stored across several non-contiguous Modbus addresses, requiring you to extract information from both coils and holding registers. Your goal is to retrieve specific values from the system to reconstruct a 4-digit access code.

Flag format: DELOGRAND{####}

# Hints
Does the server seem down? We heard a smart way to hide your devices is to change the default port that applications run on.

The code is 4 numeric digits. coils represent discrete binary values. What integers commonly correspond to on/off or true/false

# Solution
This server is running on port 5020, first you would want to nmap the device to determine which ports are open. The most surefire way would be using the modbus-discover nmap script:
`nmap x.x.x.x --script modbus-discover -p-`
For the last problem you likely didn't have to specify a port because most tools will use 502 if no tool is specified. For this one, you'll need to explicitly include the port. 

You can start by polling the registers again using the same tools you did in challenge 1. You'd notice some are set, but there is also a contiguous block that appears to be in ascii range. Decode it, and you get: code=coil5+coil17+reg3+reg22

So, simply poll these values and you get 1, 0, 7, 3. The hint makes it explicit, but coils store discrete values like on/off or true/false. These are represented with 1/0 as is often the case.