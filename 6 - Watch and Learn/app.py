from flask import Flask, render_template_string
from pymodbus.client import ModbusTcpClient
import threading
import time

app = Flask(__name__)

# Configuration for the Modbus server
MODBUS_SERVER_IP = "172.18.6.2"
MODBUS_SERVER_PORT = 5020

# Global variables to hold the sensor value and flag text
sensor_value = None
status = None

def modbus_polling():
    global sensor_value, status
    client = ModbusTcpClient(MODBUS_SERVER_IP, port=MODBUS_SERVER_PORT)
    while True:
        if client.connect():
            # Read the sensor value from holding register 1 (0-based indexing)
            result = client.read_holding_registers(10)
            if not result.isError():
                sensor_value = result.registers[0]
            else:
                sensor_value = "Error reading sensor"
                
            # Attempt to read flag from holding registers starting at address 50
            flag_result = client.read_holding_registers(address=50, count=25)
            if (flag_result.registers[0] == 0):
                status = "Normal"
            elif not flag_result.isError():
                # Convert registers (assumed to be ASCII values) to a string.
                # Stop at the first zero value (if any).
                flag_chars = ""
                for reg in flag_result.registers:
                    if reg == 0:
                        break
                    flag_chars += chr(reg)
                status = f"Error: {flag_chars}"
            else:
                status = "Error reading flag"

            client.close()
        else:
            sensor_value = None
            status = "Connection failed"
        time.sleep(2)  # Poll every 2 seconds

# Start the Modbus polling thread
polling_thread = threading.Thread(target=modbus_polling, daemon=True)
polling_thread.start()

# A simple HTML template to display the data
TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <title>ICS Temperature Control Panel</title>
  </head>
  <body>
    <h1>ICS Temperature Control Panel</h1>
    <p><strong>Sensor Value:</strong> {{ sensor_value }}</p>
    <p><strong>Operating Status:</strong> {{ status }}</p>
  </body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE, sensor_value=sensor_value, status=status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
