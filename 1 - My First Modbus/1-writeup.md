# Challenge - My first Modbus
A mysterious modbus device is running at x.x.x.x. The flag is stored in its holding registers, if only you could read them. 

# Solution 1
You simply need to read data from the registers. Each register holds a letter of the flag, staring with register 5. 

The server is running on port 502, the standard for Modbus TCP. For this reason, most tools will work without specifying the port. 

The simplest solution would be to use a modbus master emulator and read from the device (remember, modbus is not authenticated). You can use `mbtget` to read data in registers from a device. Mbtget uses relative addressing (ie address 0 is 40000 which is the first holding register)
```
mbtget -a 0 127.0.0.1
mbtget -a 1 127.0.0.1
mbtget -a 1 127.0.0.1
...
```

After running the command several times to figure out registers 5-26 store the flag, the following would display the entire flag. The -n option displays registers sequentially. Without doing anything special, the data is ascii encoded, so you can copy it into cyberchef or write a script
```
mbtget -n 26 -a 0 127.0.0.1
```

# Solution 2
Using the same `pymodbus` module used by the slave, you can create a client and decode the data in a single python script. See `1-solution.py`
