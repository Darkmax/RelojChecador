try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import time
import finger_reader as reader
import keypad_page as keypad

class CheckInPage(tk.Frame):

    counter = 5000

    font36 = "-family Arial -size 36 -weight bold -slant roman " \
             "-underline 0 -overstrike 0"
    font40 = "-family {Arial Black} -size 40 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"
    font48 = "-family {Arial Black} -size 48 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.construct_gui()

    #construyendo la interfaz de la ventana
    def construct_gui(self):
        '''Metodo para construir la interfaz de la ventana'''
        #Boton de configuraciones
        img = tk.PhotoImage(file='./assets/config.png')
        btn_config = tk.Button(self, image=img, padx=80, command=lambda: self.master.switch_frame(keypad.KeypadPage))
        btn_config.image = img

        #Label para mostrar el dia
        lbl_date = tk.Label(self, font=self.font40)

        #Label para mostrar el tiempo
        lbl_timer = tk.Label(self, font=self.font40)
        self.update_time(lbl_date,lbl_timer)

        #Label de retro-alimentacion
        self.lbl_feedback = tk.Label(self, font=self.font36, pady=60, fg='red')

        #Boton para checkin
        self.btn_entrada = tk.Button(self, text='Entrada', font=self.font48,
                                foreground='white', background='green'
                                ,activebackground='green2', command=self.read_finger)


        #Poniendo los widgets en la ventana
        btn_config.place(relx=0.01, rely=0.01, height=78, width=78)
        lbl_date.place(relx=0.16, rely=0.05, height=101, width=284)
        lbl_timer.place(relx=0.57, rely=0.05, height=101, width=284)
        self.btn_entrada.place(relx=0.03, rely=0.38, height=224, width=657)

    def update_time(self, lbl_date, lbl_time):
        '''Metodo para obtener el tiempo del sistema operativo'''
        date_string = time.strftime('%d/%m/') + time.strftime('%Y')[2::]
        time_string = time.strftime('%H:%M:%S')
        lbl_date.config(text=date_string)
        lbl_time.config(text=time_string)
        self.after(500, self.update_time, lbl_date, lbl_time)

    def read_finger(self):
        '''Metodo para leer la huella digital de un usuario'''
        self.btn_entrada.place_forget() #quitando de pantalla el boton
        self.lbl_feedback.configure(text='Esperando huella digital...')
        self.lbl_feedback.place(relx=0.03, rely=0.38, height=231, width=664)
        ##Buscamos usuario
        self.r = reader.CheckUser() #inicializo la clase, prendo el sensor
        CheckInPage.counter = self.r.getTimeRead()
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
        self.lbl_feedback.place_forget()
        self.btn_entrada.place(relx=0.03, rely=0.38, height=224, width=657)