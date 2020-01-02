import machine
from ssd1306 import SSD1306_SPI, SSD1306_I2C
def i2c(width,height,sclpin,sdapin,soft=True):
    if soft:
        i2c = machine.I2C(scl=machine.Pin(sclpin), sda=machine.Pin(sdapin), freq=100000)
    else:
        i2c = machine.I2C(2)
    return SSD1306_I2C(width, height, i2c)
def spi(width,height,soft=True):
    if use_spi:
        # Pyb   SSD
        # 3v3   Vin
        # Gnd   Gnd
        # X1    DC
        # X2    CS
        # X3    Rst
        # X6    CLK
        # X8    DATA
        pdc = machine.Pin('X1', machine.Pin.OUT_PP)
        pcs = machine.Pin('X2', machine.Pin.OUT_PP)
        prst = machine.Pin('X3', machine.Pin.OUT_PP)
    if soft:
        spi = machine.SPI(sck=machine.Pin('X6'), mosi=machine.Pin('X8'), miso=machine.Pin('X7'))
    else:
        spi = machine.SPI(1)
        ssd = SSD1306_SPI(width, height, spi, pdc, prst, pcs)
    return ssd
