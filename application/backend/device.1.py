import sys
import json
from time import sleep
import smbus

import ledcontroller
import illuminantKind

class Device():
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.led = ledcontroller.LEDController(self.bus, 13)
        # self.intensities = illuminantKind.CIE_DAYLIGHT2.copy()
        # self.intensities.update(illuminantKind.TEST.copy())
        self.illuminant = illuminantKind.CIE_DAYLIGHT
        self.state = {'on': False, 'illuminant': 5000, 'power': 100, 'temperature': 23.0}

    def change(self, on, illuminantName, power):

        try:
            # values = [0 for i in range(13)]
            # values2 = [0 for i in range(13)]
            # values = self.intensities[str(illuminantName)]
            # for i in range(13):
            #     values2[i] = int(float(values[i]) * (float(power) / 100.0))
            
            # self.led.write(values2)
            # self.led.sync()

            values = self.illuminant[str(illuminantName)+':'+str(power)]
            
            self.led.write(values)
            self.led.sync()

            # print "change"

            if on == True:
                self.led.on()
                # print "on"
            elif on == False:
                self.led.off()
                # print "off"
        except Exception as e:
            print "i2c device connection error."

        self.state["illuminant"] = illuminantName
        self.state["power"] = power
        self.state["on"] = on

    def changeValue(self, illuminantName, power):
        # values = [0 for i in range(13)]
        # values2 = [0 for i in range(13)]
        # values = self.intensities[str(illuminantName)]
        # for i in range(13):
        #     values2[i] = int(float(values[i]) * (float(power) / 100.0))
        
        # self.led.write(values2)
        # self.led.sync()

        values = self.illuminant[str(illuminantName)+':'+str(power)]
        
        self.led.write(values)
        self.led.sync()

        self.state["illuminant"] = illuminantName
        self.state["power"] = power

    def on(self):
        self.led.on()
        self.state["on"] = True

    def off(self):
        self.led.off()
        self.state["on"] = False

    def getState(self):
        # try:
        #     t1, t2 = self.led.readTemperature()
        #     self.state["temperature"] = t1
        # except Exception as e:
        #     print e.message

        return self.state
        
if __name__ == "__main__":
    dev = Device()
    dev.change(True, 6500, 100)

        

