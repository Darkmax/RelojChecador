try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import time
import check
import finger_reader as reader

class RelojChecador(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry('700x400')
        self.switch_frame(check.CheckInPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# class CheckInPage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         img = tk.PhotoImage(file='./assets/config.png')
#         btn_config = tk.Button(self, image=img)
#         start_label = tk.Label(self, text="This is the start page")
#         page_1_button = tk.Button(self, text="Open page one",
#                                   command=lambda: master.switch_frame(PageOne))
#         page_2_button = tk.Button(self, text="Open page two",
#                                   command=lambda: master.switch_frame(PageTwo))
#         btn_config.pack()
#         start_label.pack(side="top", fill="x", pady=10)
#         page_1_button.pack()
#         page_2_button.pack()


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        page_1_label = tk.Label(self, text="This is page one")
        start_button = tk.Button(self, text="Return to start page",
                                 command=lambda: master.switch_frame(check.CheckInPage))
        page_1_label.pack(side="top", fill="x", pady=10)
        start_button.pack()


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        page_2_label = tk.Label(self, text="This is page two")
        start_button = tk.Button(self, text="Return to start page",
                                 command=lambda: master.switch_frame(check.CheckInPage))
        page_2_label.pack(side="top", fill="x", pady=10)
        start_button.pack()


if __name__ == "__main__":
    app = RelojChecador()
    app.mainloop()


# win = Tk()
#
# win.title('Reloj Checador')
# win.geometry('700x400')
# #win.attributes('-fullscreen', 1)
#
# img = PhotoImage(file='./assets/config.png')
# btn_config = Button(win, image=img)
# btn_config.grid()
#
# #Parte para desplegar el tiempo y irlo actualizando cada medio segundo
# def UpdateTime():
#     time_string = time.strftime('%H:%M:%S')
#     lbl_timer.config(text=time_string);
#     win.after(500, UpdateTime)
#
# lbl_timer = Label(win, text='', font=('Helvetica', 60), anchor='center')
# lbl_timer.grid(row=1, column=1)
# UpdateTime()
#
#
# btn_entrada = Button(win, text='Entrada', font=('Helvetica', 60),
#                      foreground='white', background='green'
#                      ,activebackground='green2', anchor=CENTER, command=reader.readFinger)
# btn_entrada.grid(row= 2, column= 1)
#
# win.mainloop()