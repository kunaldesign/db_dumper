from tkinter import Label, Entry, Button, Tk, messagebox
import tkinter as tk
import os
import sys
import time
import pipes
import datetime
from pyglet import font


class MyWindow:

    def __init__(self, win):

        font.add_file(self.resource_path_inner(
            "fonts\\Righteous\\Righteous-Regular.ttf"))

        self.lbl1 = Label(win)
        self.lbl2 = Label(win)
        self.lbl3 = Label(win)
        self.lbl4 = Label(win)
        self.lbl5 = Label(win)
        self.lbl6 = Label(win)

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

        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Entry()
        self.t4 = Entry()
        self.t5 = Entry()
        self.t6 = Entry()

        self.t1.place(x=300, y=50)
        self.t2.place(x=300, y=100)
        self.t3.place(x=300, y=200)
        self.t4.place(x=300, y=250)
        self.t5.place(x=300, y=300)
        self.t6.place(x=300, y=350)

        self.b1 = Button(win, command=self.get_data)

        self.b1.config(text="Submit")
        self.b1.config(bg="#fac56c")
        self.b1.config(font=('Righteous-Regular', 15, 'bold'))
        self.b1.place(x=200, y=400)

    def get_data(self):
        host = str(self.t1.get())
        user = str(self.t2.get())
        password = str(self.t3.get())
        port = str(self.t4.get())
        name = str(self.t5.get())
        path = str(self.t6.get())
        backup_db(host=host, user=user, password=password,
                  port=port, name=name, path=path)

    def resource_path_inner(self, relative_path):
        self.rel_path = relative_path
        try:
            self.base_path = sys._MEIPASS2
        except Exception:
            self.base_path = os.path.abspath(".")

        return os.path.join(self.base_path, self.rel_path)


window = Tk()
mywin = MyWindow(window)
window.title('DB Dumper')
window.geometry("500x450")
window.configure(bg="#50C878")


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


window.iconphoto(False, tk.PhotoImage(
    file=resource_path('asset\\images\\dump.png')))


def backup_db(host, user, password, port, name, path):
    DB_HOST = host
    DB_USER = user
    DB_USER_PASSWORD = password
    DB_PORT = port
    DB_NAME = name
    BACKUP_PATH = path

    todays_Date = datetime.date.fromtimestamp(time.time())
    DATETIME = todays_Date.isoformat()

    TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME

    try:
        os.stat(TODAYBACKUPPATH)
    except:
        os.mkdir(TODAYBACKUPPATH)

    if os.path.exists(DB_NAME):
        multi = 1
        print("Databases file found...")
        print("Starting backup of all dbs listed in file " + DB_NAME)
    else:
        print("Databases file not found...")
        print("Starting backup of database " + DB_NAME)
        multi = 0

    if multi:
        in_file = open(DB_NAME, "r")
        flength = len(in_file.readlines())
        in_file.close()
        p = 1
        dbfile = open(DB_NAME, "r")

        while p <= flength:
            db = dbfile.readline()
            db = db[:-1]
            dumpcmd = "mysqldump -v -h " + DB_HOST + " --port=" + DB_PORT + " -u " + DB_USER + " -p" + \
                DB_USER_PASSWORD + " " + db + " > " + \
                pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
            os.system(dumpcmd)
            gzipcmd = "gzip " + \
                pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
            os.system(gzipcmd)
            p = p + 1
        dbfile.close()
    else:
        db = DB_NAME
        dumpcmd = "mysqldump -v -h " + DB_HOST + " --port=" + DB_PORT + " -u " + DB_USER + " -p" + \
            DB_USER_PASSWORD + " " + db + " > " + \
            pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
        os.system(dumpcmd)
        gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
        os.system(gzipcmd)

    print("")
    print("Backup script completed")
    print("Your backups have been created in '" +
          TODAYBACKUPPATH + "' directory")

    messagebox.showinfo("information", "Success!!")
    sys.exit()


window.mainloop()
