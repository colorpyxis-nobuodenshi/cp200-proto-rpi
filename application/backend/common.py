import sys
import os
import Queue

class MessageQueue(object):
    def __init__(self):
        self._queue = Queue.Queue()

    def enqueue(self, obj):
        self._queue.put(obj)

    def dequeue(self):
        return self._queue.get()

    def empty(self):
        return self._queue.empty()

class Handler(object):
    def __init__(self):
        self._looper = Looper.getMainLoop()
        self._message = Looper.MessageQueue()
        
    def sendMessage(self, message):
        pass

    def handleMessage(self):
        pass

    def dispatchMessage(self, message):
        pass

class Looper(object):
    def __init__(self):
        self.messageQueue = MessageQueue()

    @staticmethod
    def MessageQueue():
        return self.messageQueue

    @staticmethod
    def getMainLoop():
        return self

    def Loop(self):
        while True:
            pass
    