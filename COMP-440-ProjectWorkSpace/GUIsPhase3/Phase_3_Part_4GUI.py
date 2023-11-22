import tkinter as tk
import tkcalendar
import DatabaseControl
import MainMenuGUI
from phase3templates import UserTableGUITemplate

class Phase_3_Part4:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.db = DatabaseControl.DatabaseControl()
        self.userList = self.db.loadUserDropDownMenu()
        self.searchPage = tk.Tk()
        self.searchPage.geometry('800x500')  # 1500
        self.searchPage.title('Users who posted the most number of items on a specific date')
        self.createWidgets()
        self.formatWidgets()
        self.searchPage.mainloop()
    pass

    def createWidgets(self):
        #self.selectedUser = tk.StringVar()

        self.frame = tk.Frame()
        self.heading = tk.Label(self.frame, text='Users who posted the most number of items on a specific date', font=('Arial', 16))

        self.searchBtn = tk.Button(self.frame, bg='#CFDFEF', text='Search', font=('Arial', 16), command=self.search)
        self.backBtn = tk.Button(self.frame, bg='#CFDFEF', text='Back', font=('Arial', 16), command=self.back, width=8)
        self.dateText = tk.Label(self.frame, text='Please pick Date: ', font=('Arial', 16))
        self.calendar = tkcalendar.DateEntry(self.frame, selectmode='day', date_pattern='yyyy/mm/dd')

    pass

    def formatWidgets(self):
        self.heading.grid(row=0, column=1, columnspan=1, sticky='news', pady=10)

        self.dateText.grid(row=1, column=0, columnspan=1, sticky='news', pady=10)
        self.calendar.grid(row=1, column=1, columnspan=2, sticky='news', pady=10)

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
        self.generatedList = self.db.phase3Part4(self.calendar.get())
        mostNumItems = self.generatedList[0][5]
        self.db.myCursor.close()
        self.db.db.close()
        self.searchPage.destroy()
        headingName = 'Users who posted the most number of items on a specific date'
        table = UserTableGUITemplate.UserTableGUITemplate(self.userName, self.password, self.generatedList, headingName)
    pass