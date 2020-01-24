import time
import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from digitalio import Direction


i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c)

led_pin = mcp.get_pin(0)
led_pin.direction = Direction.OUTPUT

while True:
    led_pin.value = True
    time.sleep(0.3)
    led_pin.value = False
    time.sleep(0.3)

