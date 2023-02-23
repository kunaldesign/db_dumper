# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from tkinter import *
from models.db_main import backup_db
from views.view import label_Field, Text_Field, Button_Field, window_Field


class MyWindow:

    def __init__(self, win):

        self.lbl1 = Label(win)
        self.lbl2 = Label(win)
        self.lbl3 = Label(win)
        self.lbl4 = Label(win)
        self.lbl5 = Label(win)
        self.lbl6 = Label(win)

        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Entry()
        self.t4 = Entry()
        self.t5 = Entry()
        self.t6 = Entry()

        self.b1 = Button(win, command=self.get_data)

        label_Field(self, self.lbl1, self.lbl2, self.lbl3,
                    self.lbl4, self.lbl5, self.lbl6)
        Text_Field(self, self.t1, self.t2, self.t3, self.t4, self.t5, self.t6)
        Button_Field(self, self.b1)

    def get_data(self):
        host = str(self.t1.get())
        user = str(self.t2.get())
        password = str(self.t3.get())
        port = str(self.t4.get())
        name = str(self.t5.get())
        path = str(self.t6.get())
        backup_db(host=host, user=user, password=password,
                  port=port, name=name, path=path)


window = Tk()
mywin = MyWindow(window)
window_Field(window)
window.mainloop()
