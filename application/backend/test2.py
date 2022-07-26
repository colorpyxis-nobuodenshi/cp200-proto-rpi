import sys
import json
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

try:
    r = s.connect(('', 8001))
    s.send(json.dumps({'payload':'subscribe','message':{'eventName':'change'}}))
    time.sleep(0.1)
    s.send(json.dumps({'payload':'subscribe','message':{'eventName':'status'}}))
    # s.send(json.dumps({'payload':'publish','message':{'eventName':'change','data':{'illuminant':5500,'power':100,'on':True}}}))
    
    while True:
        print s.recv(1024)
        time.sleep(0.1)
    # data = s.recv(1024)
    # print 'Client recieved data :', str(data)
    s.close()

except socket.error, e:
    print 'Error: %s' % e