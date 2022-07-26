# import RPi.GPIO as GPIO
from time import sleep

usleep = lambda x: sleep(x/1000000.0)

LEDCON_ADR = 0x40
LEDCON_CHANNEL = 24

class LEDController():
    def __init__(self, i2c, pin):
        self.bus = i2c
        self.pin = pin
        self.onoff = 0
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.pin, GPIO.OUT)
        self.consumedElectricCurrent = 0.0
        self.consumedElectricPower = 0.0

    def __del__(self):
        # GPIO.cleanup(self.pin)
        pass

    def write(self, values):
        values1 = allocateLEDChannel(values)
        
        adr = 2
        for i in range(LEDCON_CHANNEL):
            val = values1[i]
            val1 = (val >> 8) & 0xFF
            val2 = val & 0xFF

            self.bus.write_byte_data(LEDCON_ADR, adr, val1)
            adr += 1
            self.bus.write_byte_data(LEDCON_ADR, adr, val2)
            adr += 1
            usleep(30)
            # print "no=%d,value=%d" % (i, val)

        # self.consumedElectricCurrent = self.totalCurrent(values1.copy())
        # self.consumedElectricPower = self.totalWattage(values1.copy())
        
    def sync(self):
        message = (self.onoff << 1) | 0x1
        self.bus.write_byte_data(LEDCON_ADR, 0x00, message)

    def on(self):
        # GPIO.output(self.pin, GPIO.HIGH)
        self.onoff = 1
        self.bus.write_byte_data(LEDCON_ADR, 0x00, 0x02)

    def off(self):
        # GPIO.output(self.pin, GPIO.LOW)
        self.onoff = 0
        self.bus.write_byte_data(LEDCON_ADR, 0x00, 0x00)

    def readTemperature(self):
        temp1 = self.bus.read_word_data(LEDCON_ADR, 0x50)
        temp2 = self.bus.read_word_data(LEDCON_ADR, 0x52)

        return (temp1 / 256.0, temp2 / 256.0)

    def readStatus(self):
        status = self.bus.read_byte_data(LEDCON_ADR, 0x1)
        run = status & 0x1
        error = (status >> 1) & 0x1

        return (run, error)

    def calcCurrent(self, values):
        res = []
        for v in values:
            res.append(self.calcCurrent(v))

        return res

    def totalCurrent(self, values):
        res = 0.0
        for v in values:
            res = res + self.__calcCurrent(v)

        return res

    def totalWattage(self, values):
        res = 0.0
        for v in values:
            res = res + self.__calcWattage(v)

        return res

    def __calcCurrent(self, value):
        v = value / 1023.0 * 2.048
        i = v / 5.6
        return i

    def __calcWattage(self, value):
        v = value / 1023.0 * 2.048
        i = v / 5.6
        return i * i * 5.6

def allocateLEDChannel(values):
    res = [0 for i in range(LEDCON_CHANNEL)]

    res[0] = values[0]
    res[1] = values[1]
    res[2] = values[2]
    res[3] = values[3]
    res[4] = values[4]
    res[5] = values[5]
    res[6] = values[6]
    res[7] = values[7]
    res[8] = values[8]
    res[9] = values[9]
    res[10] = values[10]
    res[11] = values[11]
    res[12] = values[11]
    res[13] = values[11]
    res[14] = values[11]
    res[15] = values[11]
    res[16] = values[12]
    res[17] = values[12]
    res[18] = values[12]
    res[19] = values[12]
    res[20] = values[12]
    res[21] = values[12]
    
    return res

if __name__ =="__main__":
    import smbus
    bus = smbus.SMBus(1)
    led = LEDController(bus, 13)
    led.write([0,0,0,0,0,0,0,0,0,0,0,1000,0])
    led.sync()
    led.on()

    # res = led.readTemperature()
    # print res
