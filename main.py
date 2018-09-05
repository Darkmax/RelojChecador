try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import checkin_page

import add_person_page as add

class RelojChecador(tk.Tk):

    _frame = None

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('700x400+1100+600')
        #self.switch_frame(checkin_page.CheckInPage) #show first frame
        self.switch_frame(add.addPersonPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

if __name__ == "__main__":
    app = RelojChecador()
    app.mainloop()