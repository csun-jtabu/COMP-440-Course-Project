import tkinter as tk
from tkinter import ttk
import DatabaseControl
import MainMenuGUI


class ReviewTableGUITemplate:
    def __init__(self, userName, password, reviewList):
        self.userName = userName
        self.password = password
        self.reviewList = reviewList
        self.db = DatabaseControl.DatabaseControl()
        self.reviewTableGUI = tk.Tk()
        self.reviewTableGUI.geometry('800x500')  # 1500
        self.reviewTableGUI.title('Reviews')
        self.createWidgets()
        self.formatWidgets()
        self.reviewTableGUI.mainloop()
    pass

    def createWidgets(self):
        self.frame = tk.Frame()

        self.backBtn = tk.Button(self.frame, bg='#CFDFEF', text='Go Back', font=('Arial', 16), command=self.goBack,
                                 width=8)

        self.table = ttk.Treeview(self.frame, columns=('productId', 'user', 'rating', 'description', 'date'),
                                  show='headings')
        self.verticalScroll = ttk.Scrollbar(self.frame, orient='vertical', command=self.table.yview)
        self.horizontalScroll = ttk.Scrollbar(self.frame, orient='horizontal', command=self.table.xview)
        self.table.configure(yscrollcommand=self.verticalScroll.set)
        self.table.configure(xscrollcommand=self.horizontalScroll.set)

        self.table.column('productId', width=15)
        self.table.column('user', width=15)
        self.table.column('rating', width=15)
        self.table.column('description', width=15)
        self.table.column('date', width=15)
        self.table.heading('productId', text='Product ID')
        self.table.heading('user', text='User')
        self.table.heading('rating', text='Rating')
        self.table.heading('description', text='Description')
        self.table.heading('date', text='Date')

    pass

    def formatWidgets(self):
        self.table.grid(row=1, column=1, columnspan=1, sticky='news', pady=10)
        self.verticalScroll.grid(row=1, column=2, sticky='ns')
        self.horizontalScroll.grid(row=2, column=1, sticky='we')

        self.backBtn.grid(row=3, column=1, columnspan=1, sticky='w', pady=10, padx=10)

        self.frame.pack()
    pass

    def goBack(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.reviewTableGUI.destroy()
        menu = MainMenuGUI.MainMenuGUI(self.userName, self.password)
    pass

    def loadTableData(self):
        if self.reviewList != None:
            counter = 0
            for review in self.reviewList:
                self.table.insert(parent='', index=counter, values=(review[0], review[1], review[2], review[3], review[4]))
                counter = counter + 1
    pass