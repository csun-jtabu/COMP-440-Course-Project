import DatabaseControl
import tkinter as tk
from tkinter import ttk

import MainMenuGUI
import SubmitReviewGUI
import ViewReviewsGUI
import ErrorBoxGUI


class SearchGUI:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.db = DatabaseControl.DatabaseControl()
        self.searchPage = tk.Tk()
        self.searchPage.geometry('800x500') #1500
        self.searchPage.title('Search')
        self.createWidgets()
        self.formatWidgets()
        self.searchPage.mainloop()
    pass

    def createWidgets(self):
        self.catSearch = tk.StringVar()

        self.frame = tk.Frame()
        self.searchText = tk.Label(self.frame, text='Search a product\n by Category: ', font=('Arial', 16))

        self.searchEntry = tk.Entry(self.frame, textvariable=self.catSearch, font=('Arial', 16), width=30)

        self.searchBtn = tk.Button(self.frame, bg='#CFDFEF', text='Search', font=('Arial', 16), command=self.search)
        self.backBtn = tk.Button(self.frame, bg='#CFDFEF', text='Go Back', font=('Arial', 16), command=self.goBack, width=8)
        self.seeReviewsBtn = tk.Button(self.frame, bg='#CFDFEF', text='See Reviews', font=('Arial', 16), command=self.viewReviews, width=10)
        self.reviewBtn = tk.Button(self.frame, bg='#CFDFEF', text='Review', font=('Arial', 16), command=self.review, width=8)

        self.table = ttk.Treeview(self.frame, columns=('ProductID','Title', 'Description', 'Category', 'Price'), show='headings')
        self.verticalScroll = ttk.Scrollbar(self.frame, orient='vertical',command=self.table.yview)
        self.horizontalScroll = ttk.Scrollbar(self.frame, orient='horizontal', command=self.table.xview)
        self.table.configure(yscrollcommand=self.verticalScroll.set)
        self.table.configure(xscrollcommand=self.horizontalScroll.set)

        self.table.column('ProductID', width=15)
        self.table.column('Title', width=15)
        self.table.column('Description', width=15)
        self.table.column('Category', width=15)
        self.table.column('Price', width=15)
        self.table.heading('ProductID', text='Product ID')
        self.table.heading('Title', text='Title')
        self.table.heading('Description', text='Description')
        self.table.heading('Category', text='Category')
        self.table.heading('Price', text='Price')
        self.loadTableData()
    pass

    def formatWidgets(self):
        self.searchText.grid(row=0, column=0, columnspan=1, sticky='news', pady=10)
        self.searchEntry.grid(row=0, column=1, columnspan=1, sticky='news', pady=10)
        self.searchBtn.grid(row=0, column=2, columnspan=1, sticky='news', pady=10)

        self.table.grid(row=1, column=1, columnspan=1, sticky='news', pady=10)
        self.verticalScroll.grid(row=1, column=2, sticky='ns')
        self.horizontalScroll.grid(row=2, column=1, sticky='we')

        self.backBtn.grid(row=3, column=1, columnspan=1, sticky='w', pady=10, padx=10)
        self.seeReviewsBtn.grid(row=3, column=1, columnspan=1, pady=10, padx=10)
        self.reviewBtn.grid(row=3, column=1, columnspan=1, sticky='e', pady=10, padx=10)


        self.frame.pack()
    pass

    def loadTableData(self):
        allItems = self.db.loadItemData()
        counter = 0
        for item in allItems:
            self.table.insert(parent='', index=counter, values=(item[0], item[1], item[2], item[3], item[4]))
            counter = counter + 1
    pass

    def search(self):
        self.clearTable()
        category = self.catSearch.get()
        self.searchTableData(category)
    pass

    def searchTableData(self, category):
        searchItems = self.db.searchByCategory(category)
        #print(searchItems)
        if searchItems != None:
            counter = 0
            for item in searchItems:
                self.table.insert(parent='', index=counter, values=(item[0], item[1], item[2], item[3], item[4]))
                counter = counter + 1
    pass

    def clearTable(self):
        for row in self.table.get_children():
            self.table.delete(row)
    pass

    def review(self):
        selectedItem = self.table.focus()
        if selectedItem:
            row = self.table.item(selectedItem)
            selectedProduct = row.get("values")[0]
            self.db.myCursor.close()
            self.db.db.close()
            self.searchPage.destroy()
            review = SubmitReviewGUI.SubmitReviewGUI(self.userName, self.password, selectedProduct)
        else:
            self.error('No product was selected. \nPlease select a product to leave a review.')
            pass

    def viewReviews(self):
        selectedItem = self.table.focus()
        if selectedItem:
            row = self.table.item(selectedItem)
            selectedProduct = row.get("values")[0]
            self.db.myCursor.close()
            self.db.db.close()
            self.searchPage.destroy()
            viewReviews = ViewReviewsGUI.ViewReviewsGUI(self.userName, self.password, selectedProduct)
        else:
            self.error('No product was selected. \nPlease select a product to view a review.')
            pass

    def error(self, text):
        error = ErrorBoxGUI.ErrorBoxGUI(text)
    pass

    def goBack(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.searchPage.destroy()
        menu = MainMenuGUI.MainMenuGUI(self.userName, self.password)
    pass

pass