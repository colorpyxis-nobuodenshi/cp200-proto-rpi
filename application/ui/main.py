#!/usr/bin/python
# -'''- coding: utf-8 -'''-

import sys
import socket
import json
import threading
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView
import redis

class Backend(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.__illuminant = 6500
        self.__power = 100
        self.__on = False
        # self.viewContext = None
        self.redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.thread1 = threading.Thread(target=self.__recive)
        self.thread1.start()
        self.stopEvent = threading.Event()

    def __del__(self):
        QObject.__del__(self)
        self.stopEvent.set()
        self.thread1.join()

    def send(self, illuminant, power, on):

        # s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # s.connect("/tmp/request.sock")
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect(("127.0.0.1", 8080))
        
        # message = json.dumps({'payload':'change', 'message': {'illuminant':illuminant, 'power': power, 'on': on}})
        # print message
        # s.send(message)
        self.redisClient.publish('change', json.dumps({'illuminant':illuminant, 'power': power, 'on': on}))
    
    def __recive(self):
        self.redisSubscriber = self.redisClient.pubsub()
        self.redisSubscriber.subscribe(['status'])
        while not self.stopEvent.is_set():
            for message in self.redisSubscriber.listen():
                if message['type'] == "message":
                    # channel = message["channel"]
                    data = json.loads(message['data'])
                    # print data
                    self.__setIlluminant(data["illuminant"])
                    self.__setPower(data["power"])
                    self.__setOnOffStatus(data["on"])

                    # self.updateView()
    @Slot()
    def upIlluminant(self):
        # print "illuminant up."
        illuminant = self.__illuminant
        power = self.__power
        on = self.__on

        if on == False:
            return

        if illuminant == 2800:
            illuminant = 3500
        elif illuminant == 3500:
            illuminant = 4300
        elif illuminant == 4300:
             illuminant = 5000
        elif illuminant == 5000:
             illuminant = 5500
        elif illuminant == 5500:
             illuminant = 6500
        elif illuminant == 6500:
             illuminant = 7500
        
        self.send(illuminant, power, on)

    @Slot()
    def downIlluminant(self):
        # print "illuminant down."
        illuminant = self.__illuminant
        power = self.__power
        on = self.__on

        if on == False:
            return

        if illuminant == 3500:
            illuminant = 2800
        elif illuminant == 4300:
             illuminant = 3500
        elif illuminant == 5000:
             illuminant = 4300
        elif illuminant == 5500:
             illuminant = 5000
        elif illuminant == 6500:
             illuminant = 5500
        elif illuminant == 7500:
             illuminant = 6500
             
        self.send(illuminant, power, on)

    @Slot()
    def upPower(self):
        # print "power up."
        illuminant = self.__illuminant
        power = self.__power
        on = self.__on
        
        if on == False:
            return

        if power == 25:
            power = 50
        elif power == 50:
            power = 75
        elif power == 75:
            power = 100

        self.send(illuminant, power, on)

    @Slot()
    def downPower(self):
        # print "power down."
        illuminant = self.__illuminant
        power = self.__power
        on = self.__on
        
        if on == False:
            return

        if power == 50:
            power = 25
        elif power == 75:
            power = 50
        elif power == 100:
            power = 75
            
        self.send(illuminant, power, on)

    @Slot()
    def onoff(self):
        # print "switch on / off."
        illuminant = self.__illuminant
        power = self.__power
        on = self.__on
        if on == True:
            on = False
        else:
            on = True

        self.send(illuminant, power, on)

    def __getIlluminant(self):
        return str(self.__illuminant) + "K"

    def __setIlluminant(self, value):
        self.__illuminant = value
        self.on_illuminantChanged.emit()

    def __getPower(self):
        return str(self.__power) + "%"
    
    def __setPower(self, value):
        self.__power = value
        self.on_powerChanged.emit()

    def __getOnOffStatus(self):
        if self.__on == True:
            return "green"
        else:
            return "gray"

    def __setOnOffStatus(self, value):
        self.__on = value
        self.on_onOffStatusChanged.emit()



    on_illuminantChanged = Signal()
    on_powerChanged = Signal()
    on_onOffStatusChanged = Signal()

    illuminant = Property(str, __getIlluminant, __setIlluminant, notify=on_illuminantChanged)
    power = Property(str, __getPower, __setPower, notify=on_powerChanged)
    onOffStatus = Property(str, __getOnOffStatus, __setOnOffStatus, notify=on_onOffStatusChanged)


backend = Backend()

app = QApplication(sys.argv)
view = QDeclarativeView()

rootObject = view.rootObject()

context = view.rootContext()
context.setContextProperty("backend", backend)

# backend.setViewContext(context)
# backend.updateView()

url = QUrl('view.qml')

view.setSource(url)
view.showFullScreen()
# view.show()

sys.exit(app.exec_())
