import sys
import json
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

try:
    r = s.connect(('', 8004))
    # s.send(json.dumps({'payload':'change','data':{'illuminant':5000, 'power': 100, 'on': True}}))
    # time.sleep(1)
    while True:
        # s.recv(1024).strip()
        data = s.recv(1024).strip()
        data = data.split('\n')[0]
        print 'Client recieved data :', str(data)
        # time.sleep(1)
    s.close()

except socket.error, e:
    print 'Error: %s' % e