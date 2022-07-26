import sys
import json
import socket
import SocketServer
import Queue
import threading
import time

requestQueue = Queue.Queue()
responseQueue = Queue.Queue()
import deviceMock

def loop(req,res):
    
    dev = deviceMock.Device()

    while True:
        r = req.get()
        payload = r['payload']
        message = r['message']
        if payload == 'change':
            on = message['on']
            illuminant = message['illuminant']
            power = message['power']
            dev.change(on, illuminant, power)
        elif payload == 'state':
            state = dev.getState()
            res.put({'payload':'state','message':state})

dev = deviceMock.Device()

class CommandHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        # print "connect from:", self.client_address
        while True:
            data = self.request.recv(1024)
            if len(data) == 0:
                break
            dev.change(True, 5000, 25)
        self.request.close()

class StatusHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        # print "connect from:", self.client_address
        self.request.settimeout(0.2)
        index = 0
        while True:
            try:
                data = dev.getState()
                data["no"] = index
                message = json.dumps(data)
                # for i in range(1024-len(message)):
                #     message = message + ' '
                self.request.send(message+'\n')
                time.sleep(0.1)
                index = index + 1
            except socket.timeout:
                continue
            except:
                break
        self.request.close()

def serverthread1():
    server = SocketServer.ThreadingTCPServer(('', 8001), CommandHandler)
    server.serve_forever()

def serverthread2():
    server = SocketServer.ThreadingTCPServer(('', 8004), StatusHandler)
    server.serve_forever()

if __name__ == '__main__':
    # t1 = threading.Thread(target=serverthread1)
    # t2 = threading.Thread(target=serverthread2)

    # t1.start()
    # t2.start()

    serverthread2()

