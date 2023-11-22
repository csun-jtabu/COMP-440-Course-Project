import tkinter as tk
from tkinter import ttk
import DatabaseControl
import ErrorBoxGUI
import MainMenuGUI


class UserTableGUITemplate:
    def __init__(self, userName, password, userList, heading):
        self.userName = userName
        self.password = password
        self.userList = userList
        self.headingName = heading
        self.db = DatabaseControl.DatabaseControl()
        self.userTableGUI = tk.Tk()
        self.userTableGUI.geometry('800x500')  # 1500
        self.userTableGUI.title('Users')
        self.createWidgets()
        self.formatWidgets()
        self.loadTableData()
        self.userTableGUI.mainloop()
    pass

    def createWidgets(self):
        self.frame = tk.Frame()

        self.heading = tk.Label(self.frame, text=self.headingName, font=('Arial', 16))

        self.table = ttk.Treeview(self.frame, columns=('userName', 'firstName', 'lastName', 'email'),
                                  show='headings')
        self.verticalScroll = ttk.Scrollbar(self.frame, orient='vertical', command=self.table.yview)
        self.horizontalScroll = ttk.Scrollbar(self.frame, orient='horizontal', command=self.table.xview)
        self.table.configure(yscrollcommand=self.verticalScroll.set)
        self.table.configure(xscrollcommand=self.horizontalScroll.set)

        self.backBtn = tk.Button(self.frame, bg='#CFDFEF', text='Go Back', font=('Arial', 16), command=self.goBack,width=8)

        self.table.column('userName', width=150)
        self.table.column('firstName', width=150)
        self.table.column('lastName', width=150)
        self.table.column('email', width=150)
        self.table.heading('userName', text='User Name')
        self.table.heading('firstName', text='First Name')
        self.table.heading('lastName', text='Last Name')
        self.table.heading('email', text='Email')

    pass

    def formatWidgets(self):
        self.heading.grid(row=0, column=1, columnspan=1, sticky='news', pady=10)
        self.table.grid(row=1, column=1, columnspan=1, sticky='news', pady=10)
        self.verticalScroll.grid(row=1, column=2, sticky='ns')
        self.horizontalScroll.grid(row=2, column=1, sticky='we')

        self.backBtn.grid(row=3, column=1, columnspan=1, sticky='w', pady=10, padx=10)

        self.frame.pack()
    pass

    def goBack(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.userTableGUI.destroy()
        menu = MainMenuGUI.MainMenuGUI(self.userName, self.password)
    pass

    def loadTableData(self):
        if self.userList != None:
            counter = 0
            for user in self.userList:
                self.table.insert(parent='', index=counter, values=(user[0], user[2], user[3], user[4]))
                counter = counter + 1
    pass