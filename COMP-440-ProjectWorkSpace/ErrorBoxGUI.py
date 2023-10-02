import tkinter as tk

class ErrorBoxGUI:
    def __init__(self, text):

        self.text = text

        self.errorPage = tk.Toplevel()
        self.errorPage.geometry('400x200')
        self.errorPage.title('Error')  # set the name of the window
        self.createWidgets()
        self.formatWidgets()
        self.errorPage.mainloop()
    pass

    def createWidgets(self):
        self.errorFrame = tk.Frame(self.errorPage)
        self.instructText = tk.Label(self.errorFrame, text=self.text, font=('Arial',14))
    pass

    def formatWidgets(self):
        self.instructText.grid(row=0, column=1, columnspan=3, sticky='news', pady=40)
        self.errorFrame.pack()
    pass

pass