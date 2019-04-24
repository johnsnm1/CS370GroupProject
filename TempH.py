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

#For tempertature/humidity sensor
#import board
import Adafruit_DHT

#For sending update emails
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Motion Sensor Setup
GPIO.setmode(GPIO.BCM) #Set GPIO to pin numbering
GPIO.setup(23, GPIO.IN) #Setup GPIO pin PIR as input
print ("Sensor initializing . . .")
time.sleep(2) #Give sensor time to startup
print ("Active")
print ("Press Ctrl+c to end program")


#Temperature/Humidity sensor setup
dht = Adafruit_DHT.DHT22

#Main while loop, can be interrupted by a faulty read from the temp/humidity
#or by a KeyboardInterrupt (ctr-c by the user)
try:
    print("Loop entered")

    while True:
        if GPIO.input(23): #If PIR pin goes high, motion is detected
            print ("Motion Detected!")
            time.sleep(5)
        try:
            humidity, temperature = Adafruit_DHT.read_retry(dht, 23)
            # Print what we got
            if humidity is not None and temperature is not None:
                print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
                time.sleep(5)
        except:
            pass

except KeyboardInterrupt: #Ctrl-c
    pass #Go to finally

finally:
    GPIO.cleanup() #reset all GPIO
    print ("Program ended")

#Sending Email Code
#Set-up for basic log-in information
me = "testpython.email.send@gmail.com"
password = "pythontestme"
you = "testpython.email.send@gmail.com"

#Set-up for the message to be send
msg = MIMEMultipart('alternative')
msg['Subject'] = "Alert"
msg['From'] = me
msg['To'] = you

html = '<html><body><p>Hi, I have the following alerts for you!</p></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)

# Specifies the server to send the email over
server = smtplib.SMTP_SSL('smtp.gmail.com')


# Login and send the email out
server.login(me, password)
server.sendmail(me, you, msg.as_string())

server.quit()
