import tkinter as tk
from tkinter import ttk
import DatabaseControl
import MainMenuGUI
from phase3templates import ItemTableGUITemplate

class Phase_3_Part3:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.db = DatabaseControl.DatabaseControl()
        self.userList = self.db.loadUserDropDownMenu()
        self.searchPage = tk.Tk()
        self.searchPage.geometry('800x500')  # 1500
        self.searchPage.title('All the items posted by user X, such that all the comments are "Excellent" or "good"')
        self.createWidgets()
        self.formatWidgets()
        self.searchPage.mainloop()
    pass

    def createWidgets(self):
        #self.selectedUser = tk.StringVar()

        self.frame = tk.Frame()
        self.heading = tk.Label(self.frame, text='All the items posted by user X, \nsuch that all the comments are "Excellent" or "good"', font=('Arial', 16))

        self.searchBtn = tk.Button(self.frame, bg='#CFDFEF', text='Search', font=('Arial', 16), command=self.search)
        self.backBtn = tk.Button(self.frame, bg='#CFDFEF', text='Back', font=('Arial', 16), command=self.back, width=8)
        self.dropDownText = tk.Label(self.frame, text='Select User X: ', font=('Arial', 16))
        self.dropDownMenu = ttk.Combobox(self.frame, values=self.userList, font=('Arial', 16))
        self.dropDownMenu.insert(0, "Select a User")
    pass

    def formatWidgets(self):
        self.heading.grid(row=0, column=1, columnspan=1, sticky='news', pady=10)

        self.dropDownText.grid(row=1, column=0, columnspan=1, sticky='news', pady=10)
        self.dropDownMenu.grid(row=1, column=1, columnspan=2, sticky='news', pady=10)

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
        self.generatedList = self.db.phase3Part3(self.dropDownMenu.get())
        self.db.myCursor.close()
        self.db.db.close()
        self.searchPage.destroy()
        headingName = 'All the items posted by user X, \nsuch that all the comments are "Excellent" or "good"'
        table = ItemTableGUITemplate.ItemTableGUITemplate(self.userName, self.password, self.generatedList, headingName)
    pass