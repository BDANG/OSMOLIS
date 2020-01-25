import time
import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from digitalio import Direction, DigitalInOut


i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c)

# for L293D IC (motor driver)
# enable_pin = mcp.get_pin(0)
enable_pin = DigitalInOut(board.D18)
enable_pin.direction = Direction.OUTPUT


coil_A_1_pin = DigitalInOut(board.D4) #mcp.get_pin(0)
coil_A_1_pin = Direction.OUTPUT

coil_A_2_pin = mcp.get_pin(board.D17)
coil_A_2_pin = Direction.OUTPUT

coil_B_1_pin = mcp.get_pin(board.D23)
coil_B_1_pin = Direction.OUTPUT

coil_B_2_pin = mcp.get_pin(board.D24)
coil_B_2_pin = Direction.OUTPUT

enable_pin.value = True

def forward(delay, steps):
    i = 0
    while i in range(0, steps):
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        i += 1


def backwards(delay, steps):
    i = 0
    while i in range(0, steps):
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        i += 1


def setStep(w1, w2, w3, w4):
    coil_A_1_pin.value = w1
    coil_A_2_pin.value = w2
    coil_B_1_pin.value = w3
    coil_B_2_pin.value = w4


while True:
    user_delay = input("Delay between steps (milliseconds)?")
    user_steps = input("How many steps forward? ")
    forward(int(user_delay) / 1000.0, int(user_steps))
    user_steps = input("How many steps backwards? ")
    backwards(int(user_delay) / 1000.0, int(user_steps))


