import tkinter as tk

import LoginPageGUI
import SearchGUI
import DatabaseControl
import InsertGUI

class MainMenuGUI:

    def __init__(self, userName, password):
        self.db = DatabaseControl.DatabaseControl()
        self.userName = userName
        self.password = password
        self.menuPage = tk.Tk()
        self.menuPage.geometry('800x500')
        self.menuPage.title('Main Menu')  # set the name of the window
        self.createWidgets()
        self.formatWidgets()
        self.menuPage.mainloop()
    pass

    def createWidgets(self):
        self.ty = tk.Label()
        self.ty = 'Thank you ' + self.userName
        self.frame = tk.Frame()  # frame holds all the widgets in the page
        self.instructText = tk.Label(self.frame, text='You Logged In!', font=('Arial', 30))
        self.tyText = tk.Label(self.frame, text=self.ty, font=('Arial', 30))

        self.insertBtn = tk.Button(self.frame, bg='#CFDFEF', text='Insert', font=('Arial', 16), command=self.insert)
        self.searchBtn = tk.Button(self.frame, bg='#CFDFEF', text='Search', font=('Arial', 16), command=self.search)
        self.initializeBtn = tk.Button(self.frame, bg='#CFDFEF', text='Initialize\nDatabase',
                                       font=('Arial', 16), command=self.initializeDB)
        self.logoutBtn = tk.Button(self.frame, bg='#F7CEE2', text='Log Out', font=('Arial', 16), command=self.logout)

    pass

    def formatWidgets(self):
        self.instructText.grid(row=0, column=1, columnspan=3, sticky='news', pady=10)
        self.tyText.grid(row=1, column=1, columnspan=3, sticky='news', pady=10)
        self.insertBtn.grid(row=2, column=0, columnspan=2, sticky='w', pady=10)
        self.searchBtn.grid(row=2, column=2, columnspan=2, sticky='e', pady=10)
        self.initializeBtn.grid(row=3, column=1, columnspan=1, sticky='w', pady=10)
        self.logoutBtn.grid(row=3, column=2, columnspan=1, sticky='e', pady=10)
        self.frame.pack()
    pass

    def search(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.menuPage.destroy()
        search = SearchGUI.SearchGUI(self.userName, self.password)
    pass

    def initializeDB(self):
        #successMessage = ErrorBoxGUI.ErrorBoxGUI('Success!\nDatabase Re-Initialized.\nRestarting Program.')
        self.db.dbInitialization()
        #newMenu = self.__init__(self.userName, self.password)
    pass

    def insert(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.menuPage.destroy()
        insert = InsertGUI.InsertGUI(self.userName, self.password)
    pass

    def logout(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.menuPage.destroy()
        login = LoginPageGUI.LoginPageGUI()
    pass
