# -*- coding: utf-8 -*-
try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import datetime
import finger_reader as backend
import keypad_page as keypad

class CheckInPage(tk.Frame):

    font36 = "-family Arial -size 36 -weight bold -slant roman " \
             "-underline 0 -overstrike 0"
    font40 = "-family {Arial Black} -size 40 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"
    font48 = "-family {Arial Black} -size 48 -weight bold -slant " \
             "roman -underline 0 -overstrike 0"

    # counter for read finger
    counter = 5000  # default value

    # Variable to check if is in or out
    checkin = True  # flag for in or out

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.b = backend.Backend()  # inicializo la clase del sensor y base de datos
        self.date_range = self.b.getConfigurationTimeRange()
        self.feedback_message = ''
        self.construct_gui()

    def changeToKeypad(self):
        del self.b  # delete backend variable
        self.master.switch_frame(keypad.KeypadPage)

    # construyendo la interfaz de la ventana
    def construct_gui(self):
        '''Metodo para construir la interfaz de la ventana'''
        #Boton de configuraciones
        img = tk.PhotoImage(file='./assets/config.png')
        btn_config = tk.Button(self, image=img, padx=80, command= self.changeToKeypad)
        btn_config.image = img

        # Label para mostrar el dia
        lbl_date = tk.Label(self, font=self.font40)

        # Label para mostrar el tiempo
        lbl_timer = tk.Label(self, font=self.font40)

        # Label de retro-alimentacion
        self.lbl_feedback = tk.Label(self, font=self.font36, pady=60, fg='red')

        # Boton para checkin
        self.btn_entrada = tk.Button(self, text='Entrada', font=self.font48,
                                foreground='white', background='green'
                                ,activebackground='green2', command=self.read_finger)

        self.update_time(lbl_date, lbl_timer) # actualizando

        #Poniendo los widgets en la ventana
        btn_config.place(relx=0.01, rely=0.01, height=78, width=78)
        lbl_date.place(relx=0.16, rely=0.05, height=101, width=284)
        lbl_timer.place(relx=0.57, rely=0.05, height=101, width=284)
        self.btn_entrada.place(relx=0.09, rely=0.38, height=224, width=657)

    def update_time(self, lbl_date, lbl_time):
        '''Metodo para obtener el tiempo del sistema operativo'''

        date_string = datetime.datetime.now().strftime('%d/%m/') + datetime.datetime.now().strftime('%Y')[2::]
        time_string = datetime.datetime.now().strftime('%H:%M:%S')
        lbl_date.config(text=date_string)
        lbl_time.config(text=time_string)

        # checo si necesito actualizar el boton
        morning_array = self.date_range[0].split(':')
        date_morning = datetime.datetime.now().replace(
            hour=int(morning_array[0]), minute=int(morning_array[1]), second=int(morning_array[2]))

        evening_array = self.date_range[1].split(':')
        if datetime.datetime.today().weekday() == 5:
            evening_array = [11,0,0]
        date_evening = datetime.datetime.now().replace(
            hour=int(evening_array[0]), minute=int(evening_array[1]), second=int(evening_array[2]))

        if date_morning <= datetime.datetime.now() <= date_evening:
            CheckInPage.checkin = True
            self.feedback_message = 'Bienvenido: '
            self.btn_entrada.configure(text='Entrada', background='green', activebackground='green2')
        else:
            CheckInPage.checkin = False
            if datetime.datetime.now() <= datetime.datetime.now().replace(hour=17, minute=30, second=0):
                self.feedback_message = u'\u00BF\u00BFC\u00F3mo??  '
            else:
                self.feedback_message = 'Gracias: '
            self.btn_entrada.configure(text='Salida', background='red', activebackground='orange red')

        self.after(500, self.update_time, lbl_date, lbl_time)

    def read_finger(self):
        '''Metodo para leer la huella digital de un usuario'''

        self.btn_entrada.place_forget() #quitando de pantalla el boton
        self.lbl_feedback.configure(text='Esperando huella digital...')
        self.lbl_feedback.place(relx=0.03, rely=0.38, height=231, width=664)
        ##Buscamos usuario
        CheckInPage.counter = self.b.getTimeRead() * 1000
        self.wait_user()

    def wait_user(self):

        result = self.b.check_user()  # leyendo huella digital
        
        if result[0]:
            CheckInPage.counter = 0
            # Ya leyo la huella digital
            if result[1] >= 0:
                self.lbl_feedback.configure(text=self.feedback_message + result[2])
                self.create_file(result)
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
        '''Method to restore the checkin button'''

        self.lbl_feedback.configure(text='')
        self.lbl_feedback.place_forget()
        self.btn_entrada.place(relx=0.09, rely=0.38, height=224, width=657)

    def create_file(self, user):
        '''Method to create the csv file with the info of the user'''

        ##Checo si me trajo bien la informacion
        if len(user) > 2:

            now = datetime.datetime.now()

            date_string = now.strftime('%Y-%m-%d')
            time_string = now.strftime('%H%M%S')
            entrada = 'entrada' if CheckInPage.checkin else 'salida'
            path = self.b.getExportPath()


            #construyo el nombre del archivo
            filename = date_string + '_' + entrada + '_' + str(user[1]) + '.csv'
            f = open(path + '/' + filename, 'w')

            #escribiendo encabezado
            f.write('nombre;apellido;dia;tiempo;entrada/salida\r\n')
            f.write(user[2] + ';' + user[3] + ';' +
                    now.strftime('%d/%m/%Y') + ';' +
                    now.strftime('%H:%M:%S') + ';' +
                    entrada + '\r\n')
            f.close()
