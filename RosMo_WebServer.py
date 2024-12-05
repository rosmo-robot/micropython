from micropyserver import MicroPyServer
import network
from secrets import WIFI_NAME, WIFI_PASS
from RosMo import RosMo
from time import sleep
from machine import Timer
import RosMo_WebInterface


def webpage():
    dist = "?"#str(int(rosmo.getDistanceCm()))
    #Template HTML
    html = RosMo_WebInterface.webpage(dist)
    return str(html)

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_NAME, WIFI_PASS)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def show_index(request):
    ''' main request handler '''
    html = webpage()
    server.send(html)

def control_action(request):
    parts = request.split('/')
    cmd = parts[1].split('?')[0]
    if cmd == "STP":
        rosmo.car.stop()
    elif cmd == "FW":
        rosmo.car.forward(.5)
    elif cmd == "L":
        rosmo.car.turn_left(.5)
    elif cmd == "R":
        rosmo.car.turn_right(.5)
    elif cmd == "CL":
        rosmo.car.curve_left(.5)
    elif cmd == "CR":
        rosmo.car.curve_right(.5)
    elif cmd == "BK":
        rosmo.car.backward(.5)
    else:
        rosmo.car.stop()
    
    
    
    html = webpage()
    server.send(html)


    
def setPhone(request):
    RosMo_WebInterface.interface = "phone"
    html = webpage()
    server.send(html)
    
def setPC(request):
    RosMo_WebInterface.interface = "PC"
    html = webpage()
    server.send(html)

#------------------CODE--------------------


rosmo = RosMo()

ip = connect()
server = MicroPyServer()
''' add routes '''
server.add_route("/", show_index)
server.add_route("/UPD", show_index)
server.add_route("/STP", control_action)
server.add_route("/FW", control_action)
server.add_route("/BK", control_action)
server.add_route("/L", control_action)
server.add_route("/R", control_action)
server.add_route("/CL", control_action)
server.add_route("/CR", control_action)
server.add_route("/PH", setPhone)
server.add_route("/PC", setPC)

''' start server '''
server.start()
