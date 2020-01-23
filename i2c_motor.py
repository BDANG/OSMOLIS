import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from digitalio import Direction


i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c)

# for L293D IC (motor driver)
#enable_pin = mcp.get_pin(0)
#enable_pin.direction = Direction.OUTPUT
#enable_pin.value = True

coil_A_1_pin = mcp.get_pin(3)
coil_A_1_pin = Direction.OUTPUT

coil_A_2_pin = mcp.get_pin(2)
coil_A_2_pin = Direction.OUTPUT

coil_B_1_pin = mcp.get_pin(1)
coil_B_1_pin = Direction.OUTPUT

coil_B_2_pin = mcp.get_pin(0)
coil_B_2_pin = Direction.OUTPUT



