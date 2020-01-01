# please rename to boot.py
import gc
gc.collect()

try:
  import usocket as socket
except:
  import socket
from machine import Pin

pin0 = Pin(0, Pin.OUT)
pin2 = Pin(2, Pin.OUT)

pin0.off()
pin2.off()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def web_page():
    if pin0.value()==1 and pin2.value()==1:
        gpio_state='up'
    if pin0.value()==1 and pin2.value()==0:
        gpio_state='right'
    if pin0.value()==0 and pin2.value()==1:
        gpio_state='left'
    if pin0.value()==0 and pin2.value()==0:
        gpio_state='stop'
    html = """
        <html>
            <head>
                <title>ESP Web Server</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="icon" href="data:,">
                <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
                    .button{
                      display: inline-block;
                      background-color: #e7bd3b;
                      border: none; border-radius: 4px; color: white;
                      padding: 16px 40px;
                      text-decoration: none;
                      font-size: 30px;
                      margin: 2px; cursor: pointer;
                    }
                    .button2{
                      display: inline-block;
                      background-color: #4286f4;
                      order: none; border-radius: 4px; color: white;
                      padding: 16px 40px;
                      text-decoration: none;
                      font-size: 30px;
                      margin: 2px; cursor: pointer;
                    }
                </style>
            </head>
            <body>
                <h1>ESP Web Server</h1>
                <p>GPIO state: <strong>""" + gpio_state + """</strong></p>
                <p>
                    <a href="/?cmd=up">
                        <button class="button">up</button>
                    </a>
                </p>
                <p>
                    <a href="/?cmd=left">
                        <button class="button2">left</button>
                    </a>
                    <a href="/?cmd=right">
                        <button class="button2">right</button>
                    </a>
                </p>
                <p>
                    <a href="/?cmd=stop">
                        <button class="button">stop</button>
                    </a>
                </p>
            </body>
        </html>"""
    return html

while True:
    try:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)
        up = request.find('/?cmd=up')
        left = request.find('/?cmd=left')
        right = request.find('/?cmd=right')
        stop = request.find('/?cmd=stop')
        print('{}:{}:{}:{}'.format(up,left,right,stop))
        if up == 6:
            pin0.on()
            pin2.on()
        if left == 6:
            pin0.off()
            pin2.on()
        if right == 6:
            pin0.on()
            pin2.off()
        if stop == 6:
            pin0.off()
            pin2.off()
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except:
        print('err')
