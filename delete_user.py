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

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #self.b = backend.Backend()  # inicializo la clase del sensor y base de datos
        #self.construct_gui()