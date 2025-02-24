from flask import Flask, render_template_string
from pymodbus.client import ModbusTcpClient
import threading
import time

app = Flask(__name__)

# Configuration for the Modbus server
MODBUS_SERVER_IP = "172.18.7.2"
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
                status = "Normal"
            else:
                sensor_value = None
                status = "Connection failed - DELOGRAND{five_big_powerplant_booms}"
                            
            client.close()
        else:
            sensor_value = None
            status = "Connection failed - DELOGRAND{five_big_powerplant_booms}"
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
