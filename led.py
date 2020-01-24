import time
import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from digitalio import Direction, DigitalInOut


led_pin = DigitalInOut(board.D18)
led_pin.direction = Direction.OUTPUT

while True:
    led_pin.value = True
    time.sleep(0.3)
    led_pin.value = False
    time.sleep(0.3)

