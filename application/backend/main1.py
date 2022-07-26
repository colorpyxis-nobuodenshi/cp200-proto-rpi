import sys
import os
import json
import socket
# import Queue
# import threading
# import multiprocessing as mp
from time import sleep

import device

dev = device.Device()

# messageQueue = mp.Queue()
# notifyMessageQueue = mp.Queue()

# class Message(object):
#     def __init__(self, msgType, msg=None):
#         self._payload = msgType
#         self._message = msg
    
#     def get_payload(self):
#         return self._payload
    
#     def set_payload(self, value):
#         self._payload = value

#     def get_message(self):
#         return self._message
    
#     def set_message(self, value):
#         self._message = value

#     payload = property(get_payload, set_message)
#     message = property(get_message, set_message)



# def requestSocketLoop(dev, messageQueue, notifyMessageQueue):
#     if os.path.exists("/tmp/request.sock") == True:
#         os.remove("/tmp/request.sock")

#     serversocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
#     serversocket.bind("/tmp/request.sock")
#     serversocket.listen(1)

#     while True:
#         conn, address = serversocket.accept()
#         while True:
#             try:
#                 msg = conn.recv(1024).strip()
#                 if not msg:
#                     break
                
#                 obj = json.loads(msg)
#                 payload = obj["payload"]
#                 message = obj["message"]
#                 print message
#                 # messageQueue.put(Message(payload, message))
                
#                 dev.change(message["on"], message["illuminant"], message["power"])
#                 res = dev.getState()

#                 # print "return message."
#                 # res = notifyMessageQueue.get()
#                 conn.sendall(json.dumps({'payload':'state', 'message':res}))
#                 # conn.sendall(res)
#             except:
#                 continue

#         conn.close()

# # notification_stop_event = threading.Event()

# def responseSocketLoop(messageQueue, notifyMessageQueue):
#     if os.path.exists("/tmp/response.sock") == True:
#         os.remove("/tmp/response.sock")

#     serversocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
#     serversocket.bind("/tmp/response.sock")
#     serversocket.listen(1)
#     while True:
#         conn, address = serversocket.accept()
#         # t = threading.Thread(target=devicenotificationloop)
#         # t.daemon = True
#         # t.start()
#         # notification_stop_event.clear()

#         while True:
#             try:
#                 msg = notifyMessageQueue.get(False)
#                 if not msg:
#                     sleep(0.1)
#                     continue
#                 print msg.message
#                 # conn.sendall(json.dumps(msg.message))
#                 conn.sendall(json.dumps({'payload':msg.payload, 'message':msg.message}))
#             except Exception:
#                 # print Exception.message
#                 break

#         conn.close()
#         # notification_stop_event.set()
#         # print "client error."

# def devicenotificationloop():
#     # print notification_stop_event.is_set()
#     while not notification_stop_event.is_set():
#         messageQueue.put(Message("state"))
#         sleep(0.2)
#     # print "device state loop end."
#     while not messageQueue.empty():
#         messageQueue.get()

# def loop(dev, messageQueue, notifyMessageQueue):    
#     while True:
#         msg = messageQueue.get()
#         if not msg:
#             break

#         msgType = msg.payload
    
#         if msgType == "on":
#             dev.on()
#         elif msgType == "off":
#             dev.off()
#         elif msgType == "change":
#             # print msg.message
#             value = msg.message
#             messageQueue.put(Message("state"))
#             dev.change(value["on"], value["illuminant"], value["power"])
            
#         elif msgType == "state":
#             state = dev.getState()
#             # print state
#             if notifyMessageQueue.full() == False:
#                 notifyMessageQueue.put(Message("state", state))

if __name__ == "__main__":

    print "backend process start."

    # os.system('sudo systemctl start frontendservice')

    if os.path.exists("/tmp/request.sock") == True:
        os.remove("/tmp/request.sock")

    serversocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    serversocket.bind("/tmp/request.sock")
    serversocket.listen(1)

    while True:
        conn, address = serversocket.accept()
        while True:
            try:
                msg = conn.recv(1024).strip()
                if not msg:
                    break
                
                obj = json.loads(msg)
                payload = obj["payload"]
                message = obj["message"]
                print message                
                dev.change(message["on"], message["illuminant"], message["power"])
                res = dev.getState()

                conn.sendall(json.dumps({'payload':'state', 'message':res}))
            except:
                continue

        conn.close()

    # os.system('sudo systemctl stop frontendservice')