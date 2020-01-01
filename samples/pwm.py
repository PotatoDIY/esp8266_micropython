from machine import Pin, PWM
import time, math

#pwm0 = PWM(Pin(0))      # create PWM object from a pin
#pwm0.freq()             # get current frequency
#pwm0.freq(1000)         # set frequency
#pwm0.duty()             # get current duty cycle
#pwm0.duty(200)          # set duty cycle
#pwm0.deinit()           # turn off PWM on the pin

#pwm0 = PWM(Pin(0), freq=800, duty=1000) #max 1023 min 0 create and configure in one go

#gpio2 = Pin(2,Pin.OUT)
#gpio0 = Pin(0,Pin.OUT)

pwm1 = PWM(Pin(1,Pin.OUT), freq=20, duty=10) # create and configure in one go

pwm3 = PWM(Pin(3,Pin.OUT), freq=20, duty=10) # create and configure in one go#gpio2.off()
#gpio0.off()
#pwm2.deinit() 
