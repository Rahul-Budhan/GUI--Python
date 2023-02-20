from tkinter import *

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

        self.userName=Label(self,text="Username",font="8")
        self.userName.place(x=200,y=150)

        self.password=Label(self,text="Password",font="9")
        self.password.place(x=200,y=200)

    def Entry(self):
        self.userName= Text(self,borderwidth=0,highlightthickness=0,width=22,height=1)
        self.userName.place(x=320,y=155)

        self.password= Entry(self,borderwidth=0,highlightthickness=0,show="*")
        self.password.place(x=320,y=205,width=175,height=20)


if __name__=="__main__":
    Login= login()
    Login.Label()
    Login.Entry()
    Login.mainloop()