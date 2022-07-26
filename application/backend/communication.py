import os
import sys
import json
import socket
import select
import logging

class HandlerSocket(object):
    def __init__(self, socket, fileno):
        self.socket = socket
        self.fineno = fileno

    def sendMessage(self, message):
        self.socket.send(message)

    def handleMessage(self):
        message = self.socket.recv(1024)

    def handleConnected(self):
        pass

    def handleClose(self):
        pass

class ServerSocket(object):
    def __init__(self, socketName):
        self._serversocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._serversocket.bind(socketName)
        self._serversocket.listen(1)
        self._listeners = [self._serversocket]
        self._connections = {}

    def run(self):
        while True:
            rready, wready, eready = select.select(self._listeners, [], self._listeners, 0.5)

            for s in rready:
                if s == self._serversocket:
					try:
						conn, address = self._serversocket.accept()
						conn.setblocking(0)
						fileno = conn.fileno()
                        hs = HandlerSocket(conn, fileno)
                        hs.handleConnected()
						self._listeners.append(conn)
						self._connections[fileno] = hs

					except Exception as n:

						logging.debug(str(address) + ' ' + str(n))

						if conn is not None:
							conn.close()
				else:
					client = self._connections[s]
					try:
						client.handleMessage()
					except Exception as n:
                        try:
                            client.handleClose()
                        except:
                            pass

                        del self._connections[fileno]
						self.listeners.remove(s)