#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import admin_menu_page as admin_menu
import finger_reader as backend


class DeleteUserPage(tk.Frame):

    arial30 = "-family Arial -size 30 -weight bold -slant roman " \
              "-underline 0 -overstrike 0"
    arial14 = "-family Arial -size 14 -weight bold -slant roman " \
              "-underline 0 -overstrike 0"

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #self.b = backend.Backend()  # inicializo la clase del sensor y base de datos
        self.construct_gui()

    def construct_gui(self):

        img = tk.PhotoImage(file='./assets/arrow.png')
        btn_back = tk.Button(self, image=img, command=lambda: self.master.switch_frame(admin_menu.AdminMenuPage))
        btn_back.image = img
        btn_back.place(relx=0.01, rely=0.01, height=78, width=78)

        lbl_title = tk.Label(self, text='Borrar Usuarios', font=DeleteUserPage.arial30)
        lbl_title.place(relx=0.125, rely=0.03, height=51, width=414)

        ##Button delete
        self.btn_delete = tk.Button(self, text='Borrar', font=DeleteUserPage.arial14, state=tk.DISABLED,
                                 command=self.deleteUser)
        self.btn_delete.place(relx=0.84, rely=0.03, height=60, width=100)

    def deleteUser(self):
        pass