try:
    import tkinter as tk    #python 3
    from tkinter import font as tkfont  #python 3
except:
    import Tkinter as tk   #python 2
    import tkFont as tkfont    #python 2

import checkin_page

class RelojChecador(tk.Tk):

    _frame = None

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('700x400')
        self.switch_frame(checkin_page.CheckInPage) #show first frame

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        page_1_label = tk.Label(self, text="This is page one")
        start_button = tk.Button(self, text="Return to start page",
                                 command=lambda: master.switch_frame(checkin_page.CheckInPage))
        page_1_label.pack(side="top", fill="x", pady=10)
        start_button.pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        page_2_label = tk.Label(self, text="This is page two")
        start_button = tk.Button(self, text="Return to start page",
                                 command=lambda: master.switch_frame(checkin_page.CheckInPage))
        page_2_label.pack(side="top", fill="x", pady=10)
        start_button.pack()

if __name__ == "__main__":
    app = RelojChecador()
    app.mainloop()