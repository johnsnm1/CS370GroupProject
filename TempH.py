#!/usr/bin/env python3
#So I have basic functionality set up for both of the sensors that we have
#we do need to specify which pins each of the sensors is attached to and how
#we want to aggregate data (every second, every .3 seconds, etc) and then how we would
#like to format the final email that we send out

#We could also have it send motion sensor data every time motion is detected and
#send tempertature/humidity statistics every 15 minutes or however long we want

#For the motion sensor

import RPi.GPIO as GPIO
import time
from message_send import *

#For tempertature/humidity sensor
#import board
import Adafruit_DHT

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
            
        def toString(self) :
            returnString = 'The current temperature is {:.1f}C and the current humidity is {:.1f}% \n The average temperature over the last five minutes was  {:.1f}C and the average humidity was {:.1f}% <br>'.format(
                            self.currentTemp, self.currentHumid, self.currentTemperatureAverage, self.currentHumidityAverage)
            
            return returnString
        def reset(self):
            self.currentTemp = 0
            self.currentHumid = 0
            self.cumulitiveTemp = 0
            self.cumulitiveHumidity = 0
            self.currentTemperatureAverage = 0
            self.currentHumidityAverage = 0
            self.accessTimes = 0
            


datum = Datum()
#Motion Sensor Setup
GPIO.setmode(GPIO.BCM) #Set GPIO to pin numbering
GPIO.setup(24, GPIO.IN) #Setup GPIO pin PIR as input
print ("Sensor initializing . . .")
time.sleep(2) #Give sensor time to startup
print ("Active")
print ("Press Ctrl+c to end program")


#Temperature/Humidity sensor setup
dht = Adafruit_DHT.DHT22

#Main while loop, can be interrupted by a faulty read from the temp/humidity
#or by a KeyboardInterrupt (ctr-c by the user)
motion_detected = 0


email = input("Enter an email")


while True:
    five = time.time() + (60*1)
    try:
        print("Loop entered")

        while time.time() < five:
            if GPIO.input(24): #If PIR pin goes high, motion is detected
                print('Motion detected!')
                motion_detected += 1
                time.sleep(2)
            humidity, temperature = Adafruit_DHT.read_retry(dht, 23)
            #Add what we got to a running total
            if humidity is not None and temperature is not None:
                datum.update(temperature,humidity)
            time.sleep(.1)
        
        motion_string = 'Motion was detected ' + str(motion_detected) + ' times over the last five minutes\n'
        sendEmail(email, datum.toString(), motion_string)
        motion_detected = 0
        datum.reset()
            
    except KeyboardInterrupt: #Ctrl-c
        break
        pass #Go to finally

    finally:
        GPIO.cleanup() #reset all GPIO

print ("Program ended")




