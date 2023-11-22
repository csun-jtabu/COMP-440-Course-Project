import tkinter as tk
import DatabaseControl
import MainMenuGUI
from phase3templates import UserTableGUITemplate

class Phase_3_Part2:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.db = DatabaseControl.DatabaseControl()
        self.searchPage = tk.Tk()
        self.searchPage.geometry('800x500')  # 1500
        self.searchPage.title('Users who posted 2 different items same day')
        self.createWidgets()
        self.formatWidgets()
        self.searchPage.mainloop()
    pass

    def createWidgets(self):
        self.cat1 = tk.StringVar()
        self.cat2 = tk.StringVar()

        self.frame = tk.Frame()
        self.heading = tk.Label(self.frame, text='Users who posted 2 different items on same day', font=('Arial', 16))

        self.searchBtn = tk.Button(self.frame, bg='#CFDFEF', text='Search', font=('Arial', 16), command=self.search)
        self.backBtn = tk.Button(self.frame, bg='#CFDFEF', text='Back', font=('Arial', 16), command=self.back, width=8)
        self.cat1Text = tk.Label(self.frame, text='Category 1: ', font=('Arial', 16))
        self.cat1Entry = tk.Entry(self.frame, textvariable=self.cat1, font=('Arial', 16), width=30)
        self.cat2Text = tk.Label(self.frame, text='Category 2: ', font=('Arial', 16))
        self.cat2Entry = tk.Entry(self.frame, textvariable=self.cat2, font=('Arial', 16), width=30)
    pass

    def formatWidgets(self):
        self.heading.grid(row=0, column=1, columnspan=1, sticky='news', pady=10)

        self.cat1Text.grid(row=1, column=0, columnspan=1, sticky='news', pady=10)
        self.cat1Entry.grid(row=1, column=1, columnspan=2, sticky='news', pady=10)
        self.cat2Text.grid(row=2, column=0, columnspan=1, sticky='news', pady=10)
        self.cat2Entry.grid(row=2, column=1, columnspan=2, sticky='news', pady=10)

        self.backBtn.grid(row=3, column=0, columnspan=1, sticky='news', pady=10)
        self.searchBtn.grid(row=3, column=1, columnspan=1, sticky='news', pady=10)
        self.frame.pack()
    pass

    def back(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.searchPage.destroy()
        menu = MainMenuGUI.MainMenuGUI(self.userName, self.password)
    pass

    def search(self):
        self.generatedList = self.db.phase3Part2(self.cat1.get(), self.cat2.get())
        print(self.generatedList)
        self.db.myCursor.close()
        self.db.db.close()
        self.searchPage.destroy()
        headingName = 'Users who posted 2 different items same day'
        table = UserTableGUITemplate.UserTableGUITemplate(self.userName, self.password, self.generatedList, headingName)
        #table.extraInfo('')
    pass