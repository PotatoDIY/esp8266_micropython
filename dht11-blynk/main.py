import BlynkLib
from BlynkTimer import BlynkTimer
import network
import machine
import dht


WIFI_SSID = 'wifi'
WIFI_PASS = '123456'

BLYNK_AUTH = 'key'

print("Connecting to WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    pass

print('IP:', wifi.ifconfig()[0])

print("Connecting to Blynk...")
#blynk = BlynkLib.Blynk(BLYNK_AUTH,server="192.168.1.7",port=8080)
blynk = BlynkLib.Blynk(BLYNK_AUTH)
d = dht.DHT11(machine.Pin(13))

@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')

@blynk.on("disconnected")
def blynk_disconnected():
    print('Blynk disconnected')

def send(): 
    d.measure()
    blynk.virtual_write(0,d.temperature())
    blynk.virtual_write(1,d.humidity())

timer = BlynkTimer()
timer.set_interval(5, send)

while True:
    blynk.run()
    timer.run()
