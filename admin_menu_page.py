#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import checkin_page as checkin
import add_person_page as addPerson

class AdminMenuPage(tk.Frame):

    arial40 = '-family Arial -size 40 -weight bold -slant roman '  \
            '-underline 0 -overstrike 0'

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.construct_gui()

    def construct_gui(self):
        '''Construct the gui of the admin menu page'''
        #Button back
        img = tk.PhotoImage(file='./assets/arrow.png')
        btn_back = tk.Button(self, image=img, command=lambda: self.master.switch_frame(checkin.CheckInPage))
        btn_back.image = img
        btn_back.place(relx=0.01, rely=0.01, height=78, width=78)

        lbl_title = tk.Label(self, text='Elige una opción:', font=AdminMenuPage.arial40)
        lbl_title.place(relx=0.17, rely=0.05, height=91, width=484)

        btn_delUser = tk.Button(self, text='Remover\nPersona', font=AdminMenuPage.arial40, background='red', foreground='white', command=lambda: self.master.switch_frame())
        btn_delUser.place(relx=0.03, rely=0.33, height=250, width=300)

        btn_addUser = tk.Button(self, text='Agregar\nPersona', font=AdminMenuPage.arial40, background='green', activebackground='green2', command=lambda: self.master.switch_frame(addPerson.addPersonPage))
        btn_addUser.place(relx=0.54, rely=0.33, height=250, width=300)