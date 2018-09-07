#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import admin_menu_page as admin_menu
import finger_reader as reader

class addPersonPage(tk.Frame):

    arial30 = "-family Arial -size 30 -weight bold -slant roman " \
             "-underline 0 -overstrike 0"
    arial16 = "-family Arial -size 16 -weight bold -slant roman " \
             "-underline 0 -overstrike 0"
    arial14 = "-family Arial -size 14 -weight bold -slant roman " \
             "-underline 0 -overstrike 0"
    arial12 = "-family Arial -size 12 -weight bold -slant roman " \
             "-underline 0 -overstrike 0"
    arial14_n = "-family Arial -size 14 -weight normal -slant roman " \
             "-underline 0 -overstrike 0"
    arial20 = "-family Arial -size 20 -weight bold -slant roman " \
            "-underline 0 -overstrike 0"

    keys = [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '7', '8', '9'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ñ', '4', '5', '6'],
        ['MAY', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'SPC', 'DEL', '1', '2', '3'],
    ]

    mayus = False

    timer = 5000

    huella_actual = -1
    huellas = [-1,-1]

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.img_error = tk.PhotoImage(file='./assets/error32.png')
        self.img_check = tk.PhotoImage(file='./assets/ok32.png')
        self.construct_gui()

    def construct_gui(self):
        '''Construct gui of the add person page'''

        ##Button back
        img = tk.PhotoImage(file='./assets/arrow.png')
        btn_back = tk.Button(self, image=img, padx=80, command=lambda: self.master.switch_frame(admin_menu.AdminMenuPage))
        btn_back.image = img
        btn_back.place(relx=0.01, rely=0.01, height=78, width=78)

        ##Button add
        btn_add = tk.Button(self, text='Agregar', font=addPersonPage.arial14, state=tk.DISABLED)
        btn_add.place(relx=0.84, rely=0.03, height=60, width=100)

        lbl_title = tk.Label(self, text='Creación de persona', font=addPersonPage.arial30)
        lbl_title.place(relx=0.125, rely=0.03, height=51, width=414)

        ##Name fields
        lbl_name = tk.Label(self, text='Nombre:', font=addPersonPage.arial20)
        lbl_name.place(relx=0.01, rely=0.23, height=40, width=124)

        self.ent_name = tk.Entry(self, font=addPersonPage.arial12)
        self.ent_name.place(relx=0.2, rely=0.23, height=50, width=144)
        self.ent_name.focus()

        lbl_last_name = tk.Label(self, text='Apellidos:', font=addPersonPage.arial20)
        lbl_last_name.place(relx=0.46, rely=0.23, height=40, width=134)

        self.ent_lastname = tk.Entry(self, font=addPersonPage.arial12)
        self.ent_lastname.place(relx=0.66, rely=0.23, height=50, width=164)

        self.lbl_check_names = tk.Label(self, image=self.img_error)
        #self.lbl_check_names.image = self.img_error
        self.lbl_check_names.place(relx=0.93, rely=0.25, height=32, width=32)

        ##Finger print section
        lbl_finger = tk.Label(self, text='Huella:', font=addPersonPage.arial20, justify=tk.LEFT)
        lbl_finger.place(relx=0.01, rely=0.43, height=40, width=105)

        btn_finger1 = tk.Button(self, text='#1', font=addPersonPage.arial16, command=lambda: self.addFinger(0))
        btn_finger1.place(relx=0.16, rely=0.4, height=60, width=120)

        self.lbl_check1 = tk.Label(self, image=self.img_error)
        self.lbl_check1.place(relx=0.35, rely=0.43, height=32, width=32)

        btn_finger2 = tk.Button(self, text='#2', font=addPersonPage.arial16, command=lambda: self.addFinger(1))
        btn_finger2.place(relx=0.44, rely=0.4, height=60, width=120)

        self.lbl_check2 = tk.Label(self, image=self.img_error)
        self.lbl_check2.place(relx=0.64, rely=0.43, height=32, width=32)

        self.lbl_status = tk.Label(self, font=addPersonPage.arial14, foreground='red', justify=tk.LEFT)
        self.lbl_status.place(relx=0.7, rely=0.4, height=60, width=190)

        frm_keyboard = tk.Frame(self, borderwidth='2', relief=tk.GROOVE)
        frm_keyboard.place(relx=0.01, rely=0.6, width=685, height=156)

        for y, row in enumerate(addPersonPage.keys, 0):
            for x, key in enumerate(row):
                b = tk.Button(frm_keyboard, text=key, font=addPersonPage.arial12, background='grey', foreground='white', command=lambda val=key:self.code(val))
                b.place(relx=(0.01 + x * 0.0761), rely=(0.025 + y * 0.33), height=42, width=42)

        self.form_validation() ##call validation check

    def code(self, value):
        '''Method to handle the code of the keyboard'''
        if value == 'MAY':
            addPersonPage.mayus = not addPersonPage.mayus
        elif value == 'SPC':
            if self.focus_get() is not None:
                self.focus_get().insert('end', ' ')

        elif value == 'DEL':
            if self.focus_get() is not None:
                temp = self.focus_get().get()[:-1]
                self.focus_get().delete('0', 'end')
                self.focus_get().insert(0, temp)
        else:
            key = value
            if addPersonPage.mayus:
                key = key.upper()
                addPersonPage.mayus = False
            else:
                key = key.lower()

            if self.focus_get() is not None:
                self.focus_get().insert('end', key)

    def form_validation(self):
        '''Method to check the validation of the form'''
        if (len(self.ent_name.get()) < 3) or (len(self.ent_lastname.get()) < 3):
            self.lbl_check_names.configure(image=self.img_error)
        else:
            self.lbl_check_names.configure(image=self.img_check)

        self.after(1500, self.form_validation) #recall every 1.5 seconds

    def addFinger(self, num):
        if self.huellas[num] == -1:
            self.huella_actual = num
            self.r = reader.CheckUser()
            addPersonPage.timer = 10000
            self.waitUser()
        else:
            self.lbl_status.configure(text='Huella ya dada de alta')

        self.r = reader.CheckUser()
        addPersonPage.timer = 5000
        self.waitUser()


    def waitUser(self):
        result = self.r.addFinger(1)

        if result[0]:
            ##Ya leyo el dedo y le pido que lo quite
            addPersonPage.timer = 5000
            self.lbl_status.configure(text='Remueve el dedo')
            self.after(2000, self.waitUser2)
        else:
            ##Checar si leyo el dedo
            if result[1] == 1:
                ##No ha leido la huella digital
                addPersonPage.timer -= 100
                self.after(100, self.waitUser)
            elif result[1] == -1:
                #Ya leyo la huella digital pero ya existe
                addPersonPage.timer = 0
                self.lbl_status.configure(text='La huella digital ya existe')

    def waitUser2(self):
        self.lbl_status.configure(text='Pon otra vez el dedo')
        result = self.r.addFinger(2)

        if result[0]:
            ##Ya leyo el dedo otra vez
            self.timer = 0

            if self.huella_actual == 0:
                self.lbl_check1.configure(image=self.img_check)
            else:
                self.lbl_check2.configure(image=self.img_check)

            self.huellas[self.huella_actual] = result[1]
            self.lbl_status.configure(text='Huella dada de alta')
            print(result[1])
        else:
            if result[1] == 1:
                #no ha leido la huella digital por segunda vez
                addPersonPage.timer -= 100
                self.after(100, self.waitUser2)
            else:
                ##Error no es el mismo dedo
                self.timer = 0
                self.lbl_status.configure(text='No es el mismo dedo')