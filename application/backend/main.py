import sys
import os
import json
# import socket
# import Queue
# import threading
# import multiprocessing as mp
from time import sleep
from datetime import datetime

import redis

import device

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

dev = device.Device()

p = redisClient.pubsub()
p.subscribe(['change'])

while True:
    for message in p.listen():
        if message['type'] == "message":
            # channel = message["channel"]
            data = json.loads(message['data'])
            dev.change(data['on'], data['illuminant'], data['power'])
            print data

            state = dev.getState()
            print state
            redisClient.publish('status', json.dumps(state))

# deviceCommandMessageQueue = mp.Queue()
# deviceNotificationMessageQueue = mp.Queue()

# class Message(object):
#     def __init__(self, id, msg=None):
#         self._id = id
#         self._message = msg
    
#     def get_id(self):
#         return self._id
    
#     def set_id(self, value):
#         self._id = value

#     def get_message(self):
#         return self._message
    
#     def set_message(self, value):
#         self._message = value

#     id = property(get_id, set_message)
#     message = property(get_message, set_message)


# def requestMessageLoop(commandQueue, r):
#     p = r.pubsub()
#     p.subscribe(['change'])
    
#     while True:
#         for message in p.listen():
#             if message['type'] == "message":
#                 # channel = message["channel"]
#                 data = json.loads(message['data'])
#                 commandQueue.put(Message('change', data))

# def notificationMessageLoop(notificationQueue, r):
#     while True:
#         message = notificationQueue.get()
#         message.message['timestamp'] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
#         r.publish('status', json.dumps(message.message))
#         print message.message

# def deviceStatusMessageLoop(commandQueue, notificationQueue):
#     while True:
#         sleep(0.5)
#         if commandQueue.empty() == True:
#             commandQueue.put(Message("status", None))

# def deviceLoop(dev, commandQueue, notificationQueue):
#     while True:
#         msg = commandQueue.get()
#         if not msg:
#             break

#         msgType = msg.id
    
#         if msgType == "on":
#             dev.on()
#         elif msgType == "off":
#             dev.off()
#         elif msgType == "change":
#             value = msg.message
#             dev.change(value["on"], value["illuminant"], value["power"])
#         elif msgType == "status":
#             state = dev.getState()
#             # if notificationQueue.empty() == True:
#             notificationQueue.put(Message("status", state))

# if __name__ == "__main__":

#     p = mp.Process(target=deviceLoop, args=(dev, deviceCommandMessageQueue, deviceNotificationMessageQueue))
#     p.daemon = True
#     p.start()

#     p2 = mp.Process(target=deviceStatusMessageLoop, args=(deviceCommandMessageQueue, deviceNotificationMessageQueue))
#     p2.daemon = True
#     p2.start()

#     p3 = mp.Process(target=requestMessageLoop, args=(deviceCommandMessageQueue, redisClient))
#     p3.daemon = True
#     p3.start()

#     p4 = mp.Process(target=notificationMessageLoop, args=(deviceNotificationMessageQueue, redisClient))
#     p4.daemon = True
#     p4.start()

#     print "backend process start."

#     # os.system('sudo systemctl start frontendservice')

#     while True:
#         pass

#     print "backend process stop."