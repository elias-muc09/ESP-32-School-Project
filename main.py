# Language: MicroPython
# Project Name: ESP32 Simple Web Server

import socket
import network
from machine import Pin, PWM, Timer
import time
import math

# my modules
import ap
import webpage

FREQ=1000
DUTY=500
CYCLES=2
STEP_DELAY_MS=40

ap.setup_ap()

ledred = Pin(40, Pin.OUT)
ledred.off()
ledfront = Pin(38, Pin.OUT)
ledfront.off()
summer = Pin(47, Pin.OUT)
summer.value(1)

ledro1_green = PWM(Pin(7), freq=FREQ, duty=0)
ledro1_blue = PWM(Pin(15), freq=FREQ, duty=0)
ledro1_red = PWM(Pin(16), freq=FREQ, duty=0)

ledro2_green = PWM(Pin(35), freq=FREQ, duty=0)
ledro2_blue = PWM(Pin(0), freq=FREQ, duty=0)
ledro2_red = PWM(Pin(36), freq=FREQ, duty=0)

def get_ledred_state():
    if ledred.value() == 1:
        return 'ON'
    elif ledred.value() == 0:
        return 'OFF'

def get_ledfront_state():
    if ledfront.value() == 1:
        return 'ON'
    elif ledfront.value() == 0:
        return 'OFF'

def get_ledro1_state():
    if ledro1_green.duty() != 0 and ledro1_blue.duty() != 0 and ledro1_red.duty() != 0 :
        return 'ON'
    elif ledro1_green.duty() == 0 and ledro1_blue.duty() == 0 and ledro1_red.duty() == 0:
        return 'OFF'
    elif ledro1_green.duty() != 0 and ledro1_blue.duty() == 0 and ledro1_red.duty() == 0:
        return 'GREEN'
    elif ledro1_green.duty() == 0 and ledro1_blue.duty() != 0 and ledro1_red.duty() == 0:
        return 'BLUE'
    elif ledro1_green.duty() == 0 and ledro1_blue.duty() == 0 and ledro1_red.duty() != 0:
        return 'RED'

def get_ledro2_state():
    if ledro2_green.duty() != 0 and ledro2_blue.duty() != 0 and ledro2_red.duty() != 0 :
        return 'ON'
    elif ledro2_green.duty() == 0 and ledro2_blue.duty() == 0 and ledro2_red.duty() == 0:
        return 'OFF'
    elif ledro2_green.duty() != 0 and ledro2_blue.duty() == 0 and ledro2_red.duty() == 0:
        return 'GREEN'
    elif ledro2_green.duty() == 0 and ledro2_blue.duty() != 0 and ledro2_red.duty() == 0:
        return 'BLUE'
    elif ledro2_green.duty() == 0 and ledro2_blue.duty() == 0 and ledro2_red.duty() != 0:
        return 'RED'
def pulse(led_red, led_green, led_blue, t):
     for i in range(0, 60):
          led_red.duty(int(math.sin(i / 30 * math.pi) * DUTY + DUTY))
          led_green.duty(int(math.sin((i+20) / 30 * math.pi) * DUTY + DUTY))
          led_blue.duty(int(math.sin((i+40) / 30 * math.pi) * DUTY + DUTY))
          time.sleep_ms(t)

tim0 = Timer(0)

def handle_callback(timer):
    ledred.value(not ledred.value())
    ledfront.value(not ledfront.value())

#
# Debug values
#
#print("LEDRed state %s" % get_ledred_state())
#print("LEDFront state %s" % get_ledfront_state())

#
# Start webserver
#
s = ap.start_webserver()

while True:
    # Socket accept()
    conn, addr = s.accept()
    print("Got connection from %s" % str(addr))

    # Socket receive()
    request = conn.recv(1024)
    print("")
    print("")
    print("Content %s" % str(request))

    # Socket send()
    request = str(request)
    
    
    # Handle LED Red 
    ledred_on = request.find('/?LEDRED=1')
    ledred_off = request.find('/?LEDRED=0')
    
    if ledred_on == 6:
        print('LED ON')
        print(str(ledred_on))
        ledred.value(1)
        summer.value(0)
        time.sleep(1.0)
        summer.value(1)        
    elif ledred_off == 6:
        print('LED OFF')
        print(str(ledred_off))
        ledred.value(0)
        summer.value(1)
        

    # Handle LED Front 
    ledfront_on = request.find('/?LEDFRONT=1')
    ledfront_off = request.find('/?LEDFRONT=0')
    
    if ledfront_on == 6:
        print('LED ON')
        print(str(ledfront_on))
        ledfront.value(1)
    elif ledfront_off == 6:
        print('LED OFF')
        print(str(ledfront_off))
        ledfront.value(0)

    # Handle LED Room 1
    ledro1_on = request.find('/?LEDRO1=1')
    ledro1_off = request.find('/?LEDRO1=0')
    ledro1_g = request.find('/?LEDRO1=GREEN')
    ledro1_b = request.find('/?LEDRO1=BLUE')
    ledro1_r = request.find('/?LEDRO1=RED')
    ledro1_s = request.find('/?LEDRO1=SHOW')
    
    if ledro1_on == 6:
        print('LED ON')
        print(str(ledro1_on))
        ledro1_green.duty(1000)
        ledro1_blue.duty(1000)
        ledro1_red.duty(1000)
    elif ledro1_off == 6:
        print('LED OFF')
        print(str(ledro1_off))
        ledro1_green.duty(0)
        ledro1_blue.duty(0)
        ledro1_red.duty(0)
    elif ledro1_g == 6:
        print('LED GREEN')
        print(str(ledro1_g))
        ledro1_green.duty(1000)
        ledro1_blue.duty(0)
        ledro1_red.duty(0)
    elif ledro1_b == 6:
        print('LED BLUE')
        print(str(ledro1_b))
        ledro1_green.duty(0)
        ledro1_blue.duty(1000)
        ledro1_red.duty(0)
    elif ledro1_r == 6:
        print('LED RED')
        print(str(ledro1_r))
        ledro1_green.duty(0)
        ledro1_blue.duty(0)
        ledro1_red.duty(1000)
    elif ledro1_s == 6:
        print('SHOW')
        print(str(ledro1_s))
        for i in range(CYCLES):
            pulse(ledro1_red, ledro1_green, ledro1_blue, STEP_DELAY_MS)
        ledro1_green.duty(1000)
        ledro1_blue.duty(1000)
        ledro1_red.duty(1000)

    # Handle LED Room 2
    ledro2_on = request.find('/?LEDRO2=1')
    ledro2_off = request.find('/?LEDRO2=0')
    ledro2_g = request.find('/?LEDRO2=GREEN')
    ledro2_b = request.find('/?LEDRO2=BLUE')
    ledro2_r = request.find('/?LEDRO2=RED')
    ledro2_s = request.find('/?LEDRO2=SHOW')
    
    if ledro2_on == 6:
        print('LED ON')
        print(str(ledro2_on))
        ledro2_green.duty(1000)
        ledro2_blue.duty(1000)
        ledro2_red.duty(1000)
    elif ledro2_off == 6:
        print('LED OFF')
        print(str(ledro2_off))
        ledro2_green.duty(0)
        ledro2_blue.duty(0)
        ledro2_red.duty(0)
    elif ledro2_g == 6:
        print('LED GREEN')
        print(str(ledro2_g))
        ledro2_green.duty(1000)
        ledro2_blue.duty(0)
        ledro2_red.duty(0)
    elif ledro2_b == 6:
        print('LED BLUE')
        print(str(ledro2_b))
        ledro2_green.duty(0)
        ledro2_blue.duty(1000)
        ledro2_red.duty(0)
    elif ledro2_r == 6:
        print('LED RED')
        print(str(ledro2_r))
        ledro2_green.duty(0)
        ledro2_blue.duty(0)
        ledro2_red.duty(1000)
    elif ledro2_s == 6:
        print('SHOW')
        print(str(ledro2_s))
        for i in range(CYCLES):
            pulse(ledro2_red, ledro2_green, ledro2_blue, STEP_DELAY_MS)
        ledro2_green.duty(1000)
        ledro2_blue.duty(1000)
        ledro2_red.duty(1000)


    response = webpage.web_page(get_ledred_state(), get_ledfront_state(), get_ledro1_state(), get_ledro2_state())
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)

    conn.close()

