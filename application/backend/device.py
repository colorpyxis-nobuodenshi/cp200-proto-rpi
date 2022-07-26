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
        self.illuminant = illuminantKind.CIE_DAYLIGHT
        self.state = {'on': False, 'illuminant': 5000, 'power': 100, 'temperature': 23.0, 'consumedElectricCurrent':0.0, 'consumedElectricPower': 0.0}

    def change(self, on, illuminantName, power):

        try:
            values = self.illuminant[str(illuminantName)+':'+str(power)]
            
            self.led.write(values)
            self.led.sync()

            # print "change"

            if on == True:
                self.led.on()
                # print "on"
                self.state["consumedElectricCurrent"] = self.led.consumedElectricCurrent
                self.state["consumedElectricPower"] = self.led.consumedElectricPower
            elif on == False:
                self.led.off()
                # print "off"
                self.state["consumedElectricCurrent"] = 0.0
                self.state["consumedElectricPower"] = 0.0
        except Exception as e:
            print "i2c device connection error."

        self.state["illuminant"] = illuminantName
        self.state["power"] = power
        self.state["on"] = on

    def changeValue(self, illuminantName, power):

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
    print dev.state

        

