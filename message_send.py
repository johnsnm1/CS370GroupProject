#So I have basic functionality set up for both of the sensors that we have
#we do need to specify which pins each of the sensors is attached to and how
#we want to aggregate data (every second, every .3 seconds, etc) and then how we would
#like to format the final email that we send out

#We could also have it send motion sensor data every time motion is detected and
#send tempertature/humidity statistics every 15 minutes or however long we want



#For sending update emails
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




#Sending Email Code
#Set-up for basic log-in information
me = "testpython.email.send@gmail.com"
password = "pythontestme"
def sendEmail(email):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Alert"
    msg['From'] = me
    msg['To'] = email
    html = '<html><body><p>Hi, I have the following alerts for you!</p></body></html>'
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    server = smtplib.SMTP_SSL('smtp.gmail.com')
    # Login and send the email out
    server.login(me, password)
    server.sendmail(me, email, msg.as_string())
    server.quit()

#Set-up for the message to be send




# Specifies the server to send the email over

