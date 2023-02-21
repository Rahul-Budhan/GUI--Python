"""Imports made here"""
from tkinter import * 
import json


"""Login Page"""
class login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.resizable(False,False)
    def Label(self):
        print("GUI Running..")
        """Background Image"""
        self.background_image = PhotoImage(file='./img/background_image.png')
        self.background_image_label = Label(self,image=self.background_image)
        self.background_image_label.place(x=-2,y=0)

        """White Canvas"""
        self.canvas=Canvas(self,width=400,height=380)
        self.canvas.place(x=150,y=60)

        """Labels"""
        self.title=Label(self,text="Login",font="Bold 30")
        self.title.place(x=300,y=80)

        self.userName=Label(self,text="Username",font="10")
        self.userName.place(x=210,y=162)

        self.password=Label(self,text="Password",font="10")
        self.password.place(x=210,y=218)

    def Entry(self):
        self.userName= Text(self,borderwidth=1,highlightthickness=1,width=22,height=2)
        self.userName.place(x=320,y=155)

        self.password= Entry(self,borderwidth=1,highlightthickness=1,show="*")
        self.password.place(x=320,y=215,width=178,height=33)

    def Button(self):
        self.login_button_image = PhotoImage(file="./img/login_button.png")
        self.login_button=Button(self,image=self.login_button_image,command=self.Submit_function(),border=0,width=145,height=55)
        self.login_button.place(x=290,y=280)

    def verification(self,u,p):
        f = open('./db.json')
        details =json.load(f)
        u.lower()
        if u not in details.keys():
            print("enter correct username")
        elif p not in details.keys():
            print("enter correct passowrd")
        else:
            if details[u] == p:
                print("ok")
            else:
                print("wrong password")
    
        
    def login(self):
        print("GUI is running..")



