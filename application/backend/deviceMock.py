import sys
import json
from time import sleep

import illuminantKind

class Device():
    def __init__(self):
        # self.intensities = illuminantKind.CIE_DAYLIGHT2.copy()
        # self.intensities.update(illuminantKind.TEST.copy())
        self.illuminant = illuminantKind.CIE_DAYLIGHT
        self.state = {'on': False, 'illuminant': 5000, 'power': 100, 'temperature': 23.0}
    
    def change(self, on, illuminantName, power):
        # values = [0 for i in range(13)]
        # values2 = [0 for i in range(13)]
        # values = self.intensities[str(illuminantName)]
        # for i in range(13):
        #     values2[i] = int(float(values[i]) * (float(power) / 100.0))
        
        # self.led.write(values2)
        # self.led.sync()

        values = self.illuminant[str(illuminantName)+':'+str(power)]
        print values
        print illuminantName
        print power

        # self.led.write(values)
        # self.led.sync()

        self.state["illuminant"] = illuminantName
        self.state["power"] = power
        self.state["on"] = on
        
        print "change"

    def changeValue(self, illuminantName, power):
        # values = [0 for i in range(13)]
        # values2 = [0 for i in range(13)]
        # values = self.intensities[str(illuminant)]
        # for i in range(13):
        #     values2[i] = int(float(values[i]) * (float(power) / 100.0))
        
        values = self.illuminant[str(illuminantName)+':'+str(power)]
        print values
        print illuminantName
        print power

        self.state["illuminant"] = illuminantName
        self.state["power"] = power

    def on(self):
        self.state["on"] = True
        print "on"

    def off(self):
        self.state["on"] = False
        print "off"

    def getState(self):
        self.state["temperature"] = 23.5
        return self.state
        
if __name__ == "__main__":
    dev = Device()
    dev.change(True, 6500, 100)
    dev.change(True, 5500, 100)
    dev.change(True, 5000, 100)

        

