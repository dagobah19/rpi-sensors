import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# define the pins on the MCP3008 we will be using, and mapping them to the pi
# the var is the name of the chip pin/function and the number is the Pi GPIO
CLK = 11
DIN = 10
DOUT = 9
CS = 8

# define the time to wait between taking another reading, in seconds
delay = 5

# setup the chip
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=DIN, mosi=DOUT)

try:
    while True:
        v = (mcp.read_adc(0) / 1023.0) * 3.3
        # math to convert the reading into an actual distance
        dist = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439
        print("Distance {:.2f}".format(dist))
        time.sleep(delay)
except KeyboardInterrupt:
    print("Exiting program")