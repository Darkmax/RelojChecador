try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import checkin_page as check

class KeypadPage(tk.Frame):

    keys = [
        ['1','2','3','4','5'],
        ['6','7','8','9','0'],
    ]

    arial20 = '-family Arial -size 20 -weight bold -slant roman'
    arial40 = '-family Arial -size 40 -weight bold -slant roman'

    # create global variable for pin
    pin = ''  # empty string

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.construct_gui()



    def construct_gui(self):

        img = tk.PhotoImage(file='./assets/arrow.png')
        btn_back = tk.Button(self, image=img, command=lambda: self.master.switch_frame(check.CheckInPage))
        btn_back.image = img
        btn_back.place(relx=0.01, rely=0.01, height=78, width=78)

        self.lbl_pin = tk.Label(self, font=KeypadPage.arial40, text='****', background='white')
        self.lbl_pin.place(relx=0.27, rely=0.08, height=90, width=314)

        frame_keypad = tk.Frame(self)
        frame_keypad.place(relx=0.03, rely=0.4, relheight=0.56, relwidth=0.95)

        for y, row in enumerate(KeypadPage.keys, 0):
            for x, key in enumerate(row):
                b = tk.Button(frame_keypad, text=key, font=KeypadPage.arial20, command=lambda val=key:self.code(val))
                posx = 0.02 + x * 0.16
                posy = 0.04 + y * 0.49
                print(str(posx) + '-' + str(posy) + ',' + str(x))
                b.place(relx=posx, rely=posy, height=90, width=90)

        btn_del = tk.Button(frame_keypad, text='<<', font=KeypadPage.arial20, background='red')
        btn_del.place(relx=0.84, rely=0.04, height=90, width=90)

        btn_del = tk.Button(frame_keypad, text='enter', font=KeypadPage.arial20, background='green')
        btn_del.place(relx=0.84, rely=0.53, height=90, width=90)

    # #construyendo la interfaz de la ventana
    # def construct_gui(self):
    #     '''Metodo para construir la interfaz de la ventana'''
    #     # Boton de configuraciones
    #     img = tk.PhotoImage(file='./assets/config.png')
    #     btn_back = tk.Button(self, image=img, command= lambda: self.master.switch_frame(check.CheckInPage))
    #     btn_back.image = img
    #
    #     #Entry keycode
    #     self.e = tk.Entry(self)
    #     self.e.grid(row=1, column=0, columnspan=3, ipady=5)
    #
    #     ##Keypad
    #     for y, row in enumerate(KeypadPage.keys, 1):
    #         for x, key in enumerate(row):
    #             # `lambda` inside `for` has to use `val=key:code(val)`
    #             # instead of direct `code(key)`
    #             b = tk.Button(self, text=key, command=lambda val=key:self.code(val))
    #             b.grid(row=y+1, column=x+1, ipadx=10, ipady=10)
    #
    #
    #     # Poniendo los widgets en la ventana
    #     btn_back.grid(row=0, column=0)
    #
    # def code(self, value):
    #
    #     if value == '*':
    #         # remove last number from `pin`
    #         pin = KeypadPage.pin[:-1]
    #         # remove all from `entry` and put new `pin`
    #         self.e.delete('0', 'end')
    #         self.e.insert('end', pin)
    #
    #     elif value == '#':
    #         # check pin
    #
    #         if KeypadPage.pin == "3529":
    #             print("PIN OK")
    #         else:
    #             print("PIN ERROR!", KeypadPage.pin)
    #             # clear `pin`
    #             pin = ''
    #             # clear `entry`
    #             self.e.delete('0', 'end')
    #
    #     else:
    #         # add number to pin
    #         KeypadPage.pin += value
    #         # add number to `entry`
    #         self.e.insert('end', value)
    #
    #     print("Current:", KeypadPage.pin)