#!/usr/bin/python
from tkinter import *
from controller import Controller

import concurrent.futures
import threading
import time


class Application:
    def __init__(self):
        self.executing = False
        self.app = Tk()
        self.email = Email(self.app)
        self.app.title("Home info kit")
        self.startButton = Button(self.app,text="Start",command= self.exec)
        self.stopButton = Button(self.app,text="Stop",command= self.stopExecution)
        self.data = Text(self.app,bg = 'light blue')
        self.controller = Controller('',self.app)


    def start(self):
        self.email.start()
        self.data.grid()
        self.startButton.grid()
        self.stopButton.grid()
        self.app.mainloop()

    def exec(self):
        self.executing = True
        if self.executing is True:
            self.controller.setEmail(self.email.emailAddr)
            monitorThread = threading.Thread(target=self.controller.monitor())
            monitorThread.start()




    def stopExecution(self):
        self.executing = False






class Email:

    def __init__(self,app):
        self.app = app
        self.emailAddr = ''
        self.emailLabel = Label(app, text= "Email")
        self.emailInputField = Entry(app, bd= 5)
        self.submitButton = Button(app,text = "Submit",command= self.submit)

    def start(self):
        self.emailLabel.grid(row=0)
        self.emailInputField.grid(row=1)
        self.submitButton.grid(row=2)

    def submit(self):
        self.emailAddr = self.emailInputField.get()


def main():
    application = Application()
    application.start()

if __name__ == '__main__': main()

