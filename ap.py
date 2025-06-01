import network
import socket

# Set up the access point
def setup_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='school', password='13579')
    print('Access Point created')
    print('SSID: school')
    print('Password: 13579')
    print('IP address:', ap.ifconfig()[0])

# Set up the web server
def start_webserver():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    return s
