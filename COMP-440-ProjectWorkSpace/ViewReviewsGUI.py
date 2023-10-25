import DatabaseControl
import tkinter as tk
from tkinter import ttk

import SearchGUI

class ViewReviewsGUI:
    def __init__(self, userName, password):
        self.userName = userName
        self.userName = userName
        self.password = password
        self.db = DatabaseControl.DatabaseControl()
        self.viewReviewsPage = tk.Tk()
        self.viewReviewsPage.geometry('1500x520')
        self.viewReviewsPage.title('View Reviews')
        self.createWidgets()
        self.formatWidgets()
        self.viewReviewsPage.mainloop()
    pass

    def createWidgets(self):
        self.frame = tk.Frame()

        self.headingLabel = tk.Label(self.frame, text="Reviews", font=('Arial', 26))
        self.backButton = tk.Button(self.frame, text="Go Back", bg='#CFDFEF', font=('Arial', 16), command=self.goBack)
        self.selectedProductFrame = tk.LabelFrame(self.frame, text="Your Selected Product", font=('Arial', 16))
        self.table = ttk.Treeview(self.selectedProductFrame, columns=('ProductID', 'Title', 'Description', 'Category', 'Price'), show='headings', height=1)
        self.scrollableFrame = tk.LabelFrame(self.frame)
        self.scrollbar = ttk.Scrollbar(self.scrollableFrame)
        self.reviewsTable = ttk.Treeview(self.scrollableFrame, yscrollcommand=self.scrollbar.set, columns=('Author', 'Rating', 'Description'), show="headings", height=9)

        self.table.heading('ProductID', text='Product ID')
        self.table.heading('Title', text='Title')
        self.table.heading('Description', text='Description')
        self.table.heading('Category', text='Category')
        self.table.heading('Price', text='Price')

        self.reviewsTable.heading('Author', text='Author')
        self.reviewsTable.heading('Rating', text='Rating')
        self.reviewsTable.heading('Description', text='Description')
    pass

    def formatWidgets(self):
        self.headingLabel.grid(row=0, column=0, sticky='news', pady=20)
        self.backButton.grid(row=0, column=2, sticky='news', pady=20)

        self.selectedProductFrame.grid(row=1, column=0, sticky='news', pady=20)
        self.table.grid(row=0, column=0, sticky='news', padx=20, pady=20)

        self.scrollableFrame.grid(row=2, column=0, sticky='news', pady=20)
        self.scrollbar.pack(side="right", fill="y")
        self.reviewsTable.pack(fill="both")
        self.scrollbar.config(command=self.reviewsTable.yview)

        self.frame.pack()
    pass

    def goBack(self):
        self.viewReviewsPage.destroy()
        search = SearchGUI.SearchGUI(self.userName, self.password)
    pass

pass