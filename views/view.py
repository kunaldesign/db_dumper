from tkinter import *
import pyglet as pyfont


def label_Field(self, lbl1, lbl2, lbl3, lbl4, lbl5, lbl6):

    pyfont.font.add_file("fonts/Righteous/Righteous-Regular.ttf")

    self.lbl1.config(text="Hostname")
    self.lbl2.config(text="Username")
    self.lbl3.config(text="Password")
    self.lbl4.config(text="Port")
    self.lbl5.config(text="DB Name")
    self.lbl6.config(text="Path")

    self.lbl1.config(font=("Righteous-Regular", 15, 'bold'))
    self.lbl2.config(font=("Righteous-Regular", 15, 'bold'))
    self.lbl3.config(font=("Righteous-Regular", 15, 'bold'))
    self.lbl4.config(font=("Righteous-Regular", 15, 'bold'))
    self.lbl5.config(font=("Righteous-Regular", 15, 'bold'))
    self.lbl6.config(font=("Righteous-Regular", 15, 'bold'))

    self.lbl1.config(bg="#50C878")
    self.lbl2.config(bg="#50C878")
    self.lbl3.config(bg="#50C878")
    self.lbl4.config(bg="#50C878")
    self.lbl5.config(bg="#50C878")
    self.lbl6.config(bg="#50C878")

    self.lbl1.config(fg="#023020")
    self.lbl2.config(fg="#023020")
    self.lbl3.config(fg="#023020")
    self.lbl4.config(fg="#023020")
    self.lbl5.config(fg="#023020")
    self.lbl6.config(fg="#023020")

    self.lbl1.place(x=100, y=50)
    self.lbl2.place(x=100, y=100)
    self.lbl3.place(x=100, y=200)
    self.lbl4.place(x=100, y=250)
    self.lbl5.place(x=100, y=300)
    self.lbl6.place(x=100, y=350)


def Text_Field(self, t1, t2, t3, t4, t5, t6):

    self.t1.place(x=300, y=50)
    self.t2.place(x=300, y=100)
    self.t3.place(x=300, y=200)
    self.t4.place(x=300, y=250)
    self.t5.place(x=300, y=300)
    self.t6.place(x=300, y=350)


def Button_Field(self, b1):

    pyfont.font.add_file("fonts/Righteous/Righteous-Regular.ttf")
    self.b1.config(text="Submit")
    self.b1.config(bg="#008080")
    self.b1.config(font=('Righteous-Regular', 15, 'bold'))
    self.b1.place(x=200, y=400)


def window_Field(window):
    window.title('DB Dumper (by kunaldesign)')
    window.geometry("500x450")
    window.configure(bg="#50C878")
