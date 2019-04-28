#!usr/bin/python
#The intentions of creating this is to bring together the
# motion detecter and and the temperature/humidity gauge. Reason
#being is that we'd have to execute the individual scripts very many
#times. This would cause a lot of overhead with starting and stopping
#the monitors, and could possibly fry them.




import message_send



import time


class Controller:


    def __init__(self,email,parent):
        self.parent = parent
        self.email = email
       # GPIO.setmode(GPIO.BCM)  # Set GPIO to pin numbering
       # GPIO.setup(23, GPIO.IN)  # Setup GPIO pin PIR as input
        #time.sleep(2)  # Give sensor time to startup
        #self.dht = Adafruit_DHT.DHT22 #init for temp/humid sensor
        datum = Datum()
    def setEmail(self,email):
        self.email = email

    def checkMonitors(self):
        #humidity, temperature = Adafruit_DHT.read_retry(self.dht, 23)
        print("Scanning the humidity and temperature")

    def checkMotion(self):
        print("Scanning for motion")
        #try:
        #    if GPIO.input(23):
         #       message_send.sendEmail(self.email)
        #except:
        #    pass

        #finally:
        #    GPIO.cleanup()


    def monitor(self):
        while True:
            self.checkMonitors()
            self.checkMotion()
            time.sleep(15)


class Datum:
        def __init__(self):
            self.currentTemp = 0
            self.currentHumid = 0
            self.cumulitiveTemp = 0
            self.cumulitiveHumidity = 0
            self.currentTemperatureAverage = 0
            self.currentHumidityAverage = 0
            self.accessTimes = 0


        def update(self,temp,humid):
            self.accessTimes += 1
            self.currentTemp = temp
            self.currentHumid = humid
            self.cumulitiveTemp += temp
            self.cumulitiveHumidity += humid
            self.computeAverages()

        def computeAverages(self) :
            self.currentTemperatureAverage = self.cumulitiveTemp / self.accessTimes
            self.currentHumidityAverage = self.cumulitiveHumidity / self.accessTimes









