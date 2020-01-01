from machine import Pin,I2C
import ssd1306
i2c = I2C(scl=Pin(2), sda=Pin(0), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
oled.fill(0)
oled.show()
oled.text('hello',1,1)
oled.show()
