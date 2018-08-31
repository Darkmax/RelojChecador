try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import time
import finger_reader as reader

class CheckInPage(tk.Frame):

    counter = 5000

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.construct_gui()

    #construyendo la interfaz de la ventana
    def construct_gui(self):
        '''Metodo para construir la interfaz de la ventana'''
        #Boton de configuraciones
        img = tk.PhotoImage(file='./assets/config.png')
        btn_config = tk.Button(self, image=img)
        btn_config.image = img

        #Label para mostrar el tiempo
        lbl_timer = tk.Label(self, font=('Helvetica', 40), anchor='center')
        self.update_time(lbl_timer)

        #Label de retro-alimentacion
        self.lbl_feedback = tk.Label(self, font=('Helvetica', 40), pady=60, fg='red')

        #Boton para checkin
        self.btn_entrada = tk.Button(self, text='Entrada', font=('Helvetica', 60),
                                foreground='white', background='green'
                                ,activebackground='green2', anchor=tk.CENTER, command=self.read_finger)


        #Poniendo los widgets en la ventana
        btn_config.grid(row=0, column=0)
        lbl_timer.grid(row=1, column=1)
        self.btn_entrada.grid(row=2, column=1)

    def update_time(self, label):
        '''Metodo para obtener el tiempo del sistema operativo'''
        time_string = time.strftime('%H:%M:%S')
        label.config(text=time_string)
        self.after(500, self.update_time, label)

    def read_finger(self):
        '''Metodo para leer la huella digital de un usuario'''
        self.btn_entrada.grid_forget() #Quitando de pantalla el boton
        self.lbl_feedback.configure(text='Esperando huella digital...')
        self.lbl_feedback.grid(row=2, column=1) #Mostrando el label en pantalla
        ##Buscamos usuario
        CheckInPage.counter = 5000
        self.r = reader.CheckUser() #inicializo la clase, prendo el sensor
        self.wait_user()

    def wait_user(self):

        result = self.r.check_user() #leyendo hueya digital
        
        if result[0]:
            CheckInPage.counter = 0
            ##Ya leyo la huella digital
            if result[1] >= 0:
                self.lbl_feedback.configure(text='Bienvenido: ' + result[2])
                self.lbl_feedback.after(2000, self.restore_button)
            else:
                self.lbl_feedback.configure(text='Error: Huella no encontrada')
                self.lbl_feedback.after(2000, self.restore_button)
        else:
            CheckInPage.counter -= 100
            if CheckInPage.counter > 0:
                self.after(100, self.wait_user)
            else:
                self.lbl_feedback.configure(text='Error: se acabo el tiempo')
                self.lbl_feedback.after(2000, self.restore_button)


    def restore_button(self):
        del(self.r)
        self.lbl_feedback.configure(text='')
        self.lbl_feedback.grid_forget()
        self.btn_entrada.grid(row=2, column=1)