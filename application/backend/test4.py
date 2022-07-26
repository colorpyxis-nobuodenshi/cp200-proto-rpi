import sys
import json
import socket
import SocketServer
import Queue
import threading
import time

subscriptions = []
connections = []

def subscribe(eventName, sock):
    
    subscriptions.append((eventName, sock))
    print eventName

def unsubscribe(eventName):
    index = []
    i = 0
    for e,s in subscriptions:
        if e == eventName:
            index.append(i)
        i = i + 1

    for j in range(len(index)):
        del subscriptions[index[j]]

def publish(eventName, data):
    for e,s in subscriptions:
        if e == eventName:
            s.send(json.dumps({'payload':'notification','message':{'eventName':eventName, 'data': data}}))

class RequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print "connect from:", self.client_address
        # self.request.settimeout(0.2)
        index = 0
        while True:
            try:
                data = self.request.recv(1024).strip()
                obj = json.loads(data)
                payload = obj["payload"]
                message = obj["message"]
                eventName = message['eventName']
                if payload == "subscribe":
                    # print eventName
                    subscribe(eventName, self.request)
                elif payload == "unsubscribe":
                    unsubscribe(eventName)
                elif payload == "publish":
                    data = message['data']
                    publish(eventName, data)
                index = index + 1
            except socket.timeout:
                continue
            except:
                break
        self.request.close()

def serverthread():
    server = SocketServer.ThreadingTCPServer(('', 8001), RequestHandler)
    server.serve_forever()
    
def loop():
    while True:
        time.sleep(1)
        publish('status', 23.0)

if __name__ == '__main__':
    t = threading.Thread(target=loop)
    t.start()

    serverthread()
    