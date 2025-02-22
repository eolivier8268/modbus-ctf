# Challenge - Anyone can Write
You have gained access to a modbus device at x.x.x.x. You found a spec sheet for the device stating that the integer on holding register 10 is used to control the device. Can you find a way to overwrite these registers and unlock the flag?

Flag format: DELOGRAND{}

# Hints
Not sure what to overwrite the register with? How big is a modbus holding register?
https://csimn.com/MHelp-VP3-TM/vp3-tm-appendix-C.html

# Solution
See `solution.py` - the intended solution is to brute force the value in the specified register