import tkinter as tk
from tkinter import ttk
import DatabaseControl
import MainMenuGUI
import ErrorBoxGUI
from phase3templates import UserTableGUITemplate

class Phase_3_Part5:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.db = DatabaseControl.DatabaseControl()
        self.userList = self.db.loadUserDropDownMenu()
        self.searchPage = tk.Tk()
        self.searchPage.geometry('800x500')  # 1500
        self.searchPage.title('List the users who are favorited by X and Y')
        self.createWidgets()
        self.formatWidgets()
        self.searchPage.mainloop()
    pass

    def createWidgets(self):

        self.frame = tk.Frame()
        self.heading = tk.Label(self.frame, text='List the users who are favorited by X and Y', font=('Arial', 16))

        self.searchBtn = tk.Button(self.frame, bg='#CFDFEF', text='Search', font=('Arial', 16), command=self.search)
        self.backBtn = tk.Button(self.frame, bg='#CFDFEF', text='Back', font=('Arial', 16), command=self.back, width=8)
        self.dropDownText1 = tk.Label(self.frame, text='Select User X: ', font=('Arial', 16))
        self.dropDownMenu1 = ttk.Combobox(self.frame, values=self.userList, font=('Arial', 16))
        self.dropDownText2 = tk.Label(self.frame, text='Select User Y: ', font=('Arial', 16))
        self.dropDownMenu2 = ttk.Combobox(self.frame, values=self.userList, font=('Arial', 16))
        self.dropDownMenu1.insert(0, "Select a User")
        self.dropDownMenu2.insert(0, "Select a User")
    pass

    def formatWidgets(self):
        self.heading.grid(row=0, column=1, columnspan=1, sticky='news', pady=10)

        self.dropDownText1.grid(row=1, column=0, columnspan=1, sticky='news', pady=10)
        self.dropDownMenu1.grid(row=1, column=1, columnspan=2, sticky='news', pady=10)
        self.dropDownText2.grid(row=2, column=0, columnspan=1, sticky='news', pady=10)
        self.dropDownMenu2.grid(row=2, column=1, columnspan=2, sticky='news', pady=10)

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
        print(self.dropDownMenu1.get() + self.dropDownMenu2.get())
        self.generatedList = self.db.phase3Part5(self.dropDownMenu1.get(), self.dropDownMenu2.get())
        self.db.myCursor.close()
        self.db.db.close()
        if not self.generatedList:
            self.db = DatabaseControl.DatabaseControl()
            ErrorBoxGUI.ErrorBoxGUI('No users were found.')
        else:
            self.searchPage.destroy()
            headingName = 'List the users who are favorited by X and Y'
            table = UserTableGUITemplate.UserTableGUITemplate(self.userName, self.password, self.generatedList, headingName)
    pass