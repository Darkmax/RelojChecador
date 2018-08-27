try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import time
import finger_reader as reader

class CheckInPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        img = tk.PhotoImage(file='./assets/config.png')
        btn_config = tk.Button(self, image=img, command=)
        btn_config.image = img

        #Parte para desplegar el tiempo y irlo actualizando cada medio segundo
        def UpdateTime():
            time_string = time.strftime('%H:%M:%S')
            lbl_timer.config(text=time_string);
            self.after(500, UpdateTime)

        lbl_timer = tk.Label(self, text='', font=('Helvetica', 60), anchor='center')
        UpdateTime()

        lbl_feedback = tk.Label(self, text='', font=('Helvetica', 40), pady=60, fg='red')

        def readFinger():
            btn_entrada.grid_forget()
            lbl_feedback.configure(text='Esperando huella digital...')
            lbl_feedback.grid(row=2, column=1)
            recognized = reader.FingerReader.ReadFinger(self)
            if(recognized):
                lbl_feedback.configure(text='Hector Ramirez')
                lbl_feedback.update()
                time.sleep(2)
            lbl_feedback.grid_forget()
            btn_entrada.grid(row=2, column=1)




        btn_entrada = tk.Button(self, text='Entrada', font=('Helvetica', 60),
                             foreground='white', background='green'
                             ,activebackground='green2', anchor=tk.CENTER, command=readFinger)

        btn_config.grid(row=0, column=0)
        lbl_timer.grid(row=1, column=1)
        btn_entrada.grid(row=2, column=1)