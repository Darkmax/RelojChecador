try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import checkin_page as check

class KeypadPage(tk.Frame):

    keys = [
        ['1','2','3'],
        ['3','4','5'],
        ['7','8','9'],
        ['*','0','#'],
    ]

    # create global variable for pin
    pin = ''  # empty string

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.construct_gui()

        # construyendo la interfaz de la ventana
    def construct_gui(self):
        '''Metodo para construir la interfaz de la ventana'''
        # Boton de configuraciones
        img = tk.PhotoImage(file='./assets/config.png')
        btn_back = tk.Button(self, image=img, command= lambda: self.master.switch_frame(check.CheckInPage))
        btn_back.image = img

        #Entry keycode
        self.e = tk.Entry(self)
        self.e.grid(row=1, column=0, columnspan=3, ipady=5)

        ##Keypad
        for y, row in enumerate(KeypadPage.keys, 1):
            for x, key in enumerate(row):
                # `lambda` inside `for` has to use `val=key:code(val)`
                # instead of direct `code(key)`
                b = tk.Button(self, text=key, command=lambda val=key:self.code(val))
                b.grid(row=y, column=x, ipadx=10, ipady=10)


        # Poniendo los widgets en la ventana
        btn_back.grid(row=0, column=0)

    def code(self, value):

        if value == '*':
            # remove last number from `pin`
            pin = KeypadPage.pin[:-1]
            # remove all from `entry` and put new `pin`
            self.e.delete('0', 'end')
            self.e.insert('end', pin)

        elif value == '#':
            # check pin

            if KeypadPage.pin == "3529":
                print("PIN OK")
            else:
                print("PIN ERROR!", KeypadPage.pin)
                # clear `pin`
                pin = ''
                # clear `entry`
                self.e.delete('0', 'end')

        else:
            # add number to pin
            KeypadPage.pin += value
            # add number to `entry`
            self.e.insert('end', value)

        print("Current:", KeypadPage.pin)