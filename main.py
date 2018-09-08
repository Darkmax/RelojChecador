try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import checkin_page

import delete_user as delete

class RelojChecador(tk.Tk):

    _frame = None

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Reloj Checador')
        self.geometry('800x480+20+0')
        #self.attributes('-fullscreen', True)
        self.bind('<Escape>', self.toggle_fullscreen)

        #self.switch_frame(checkin_page.CheckInPage) # show first page
        self.switch_frame(delete.DeleteUserPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

    def toggle_fullscreen(self, event):
        self.attributes('-fullscreen', not self.attributes('-fullscreen'))

if __name__ == "__main__":
    app = RelojChecador()
    app.mainloop()
