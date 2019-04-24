#!/usr/bin/python
from tkinter import *


class Application:
    def __init__(self):
        self.app = Tk()
        self.email  = Email(self.app)
        self.app.title("Home info kit")
        self.startButton = Button(self.app,text="Start")
        self.data = Text(self.app,bg = 'light blue')

    def start(self):
        self.email.start()
        self.data.grid()
        self.startButton.grid()
        self.app.mainloop()



class Email:

    def __init__(self,app):
        self.app = app
        self.email = ''
        self.emailLabel = Label(app, text= "Email")
        self.emailInputField = Entry(app, bd= 5)
        self.submitButton = Button(app,text = "Submit",command= self.submit)

    def start(self):
        self.emailLabel.grid(row=0)
        self.emailInputField.grid(row=1)
        self.submitButton.grid(row=2)

    def submit(self):
        self.email = self.emailInputField.get()








def main():
    application = Application()
    application.start()

if __name__ == '__main__': main()

