
import machine
from machine import Pin
#import time
import esp
#import esp32
from machine import Timer

machine.freq(160000000)
esp.osdebug(None)

pR0g1, pR1g1, pR2g1, pR3g1 = Pin(25 ,Pin.IN),Pin(33 ,Pin.IN),Pin(32 ,Pin.IN),Pin(35 ,Pin.IN)
pR0g2, pR1g2, pR2g2, pR3g2 = Pin(5 ,Pin.OUT),Pin(18 ,Pin.OUT),Pin(19 ,Pin.OUT),Pin(21 ,Pin.OUT)
Button, GPIO_R3_Button = Pin(4, Pin.IN), Pin(13, Pin.OUT)

def repeter_g1tog2():
    pR0g2.value(pR0g1.value())
    pR1g2.value(pR1g1.value())
    pR2g2.value(pR2g1.value())
    pR3g2.value(pR3g1.value())
    
def repeter_button():
    if Button.value() == 1:
        GPIO_R3_Button.value(1)
    else:
        GPIO_R3_Button.value(0)

timer1 = Timer(-1)
timer2 = Timer(-2)
timer1.init(period=250, mode=Timer.PERIODIC, callback= lambda t:repeter_g1tog2())
timer2.init(period=1000, mode=Timer.PERIODIC, callback= lambda t:repeter_button())


