import machine
from writer import Writer
from writer import ssd1306_setup
from writer import courier20 as font
import gfx

ssd = ssd1306_setup.i2c(128,32,sclpin=2,sdapin=0)
wri=Writer.Writer(ssd, font,False)
wri.set_textpos(ssd, x=10, y=10)
wri.printstring('哈哈')
ssd.pixel(10,10,1)
ssd.show()
g=gfx.GFX(128,32,ssd.pixel)
g.fill_rect(0,0,20,20,1)
ssd.show()
