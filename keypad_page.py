try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import checkin_page as checkin
import admin_menu_page as admin_page
import sqlite3
import hashlib

class KeypadPage(tk.Frame):

    keys = [
        ['1','2','3','4','5','<<'],
        ['6','7','8','9','0','enter'],
    ]

    arial20 = '-family Arial -size 20 -weight bold -slant roman'
    arial40 = '-family Arial -size 40 -weight bold -slant roman'

    # create global variable for pin
    pin = ''  # empty string

    #sha = hashlib.sha256()

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.construct_gui()



    def construct_gui(self):

        img = tk.PhotoImage(file='./assets/arrow.png')
        btn_back = tk.Button(self, image=img, command=lambda: self.master.switch_frame(checkin.CheckInPage))
        btn_back.image = img
        btn_back.place(relx=0.01, rely=0.01, height=78, width=78)

        self.entry_pin = tk.Entry(self, font=KeypadPage.arial40, justify='center', show='*')
        self.entry_pin.place(relx=0.27, rely=0.08, height=90, width=314)

        img_error = tk.PhotoImage(file='assets/error.png')
        self.lblError = tk.Label(self,image=img_error)
        self.lblError.image = img_error

        frame_keypad = tk.Frame(self)
        frame_keypad.place(relx=0.03, rely=0.4, relheight=0.56, relwidth=0.95)

        for y, row in enumerate(KeypadPage.keys, 0):
            for x, key in enumerate(row):
                b = tk.Button(frame_keypad, text=key, font=KeypadPage.arial20, command=lambda val=key:self.code(val))
                b.place(relx=(0.02 + x * 0.16), rely=(0.04 + y * 0.49), height=90, width=90)
                if key == '<<':
                    b.configure(background='red', activebackground='orange red',)
                elif key == 'enter':
                    b.configure(background='green', activebackground='green2')

    def getPassword(self):
        conn = sqlite3.connect('./DB/reloj_checador.db')
        c = conn.cursor()
        c.execute('SELECT admin_password FROM Configuration WHERE idConfig=1')
        password = c.fetchone()[0]
        c.close()
        conn.close()
        return password


    def code(self, value):

        if value == '<<':
            # remove last number from `pin`
            KeypadPage.pin = KeypadPage.pin[:-1]
            # remove all from `entry` and put new `pin`
            self.entry_pin.delete('0', 'end')
            self.entry_pin.insert('end', KeypadPage.pin)

        elif value == 'enter':
            #get pin from DB
            password = self.getPassword()
            # check pin
            if hashlib.sha256(KeypadPage.pin.encode() + b'ads').hexdigest() == password:
                self.master.switch_frame(admin_page.AdminMenuPage)
            else:
                self.lblError.place(relx=0.75, rely=0.15, height=45, width=45)
                self.after(2000, self.lblError.place_forget)
                # clear `pin`
                KeypadPage.pin = ''
                # clear `entry`
                self.entry_pin.delete('0', 'end')

        else:
            # add number to pin
            KeypadPage.pin += value
            # add number to `entry`
            self.entry_pin.insert('end', value)