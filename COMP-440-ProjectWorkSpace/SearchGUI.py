import mysql.connector.errors

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
        self.searchPage.geometry('1000x500') #1500
        self.searchPage.title('Search')
        self.createWidgets()
        self.formatWidgets()
        self.searchPage.mainloop()
    pass

    def createWidgets(self):
        self.catSearch = tk.StringVar()
        self.checkBoxVar = tk.IntVar()

        self.frame = tk.Frame()
        self.searchText = tk.Label(self.frame, text='Search a product\n by Category: ', font=('Arial', 16))

        self.searchEntry = tk.Entry(self.frame, textvariable=self.catSearch, font=('Arial', 16), width=30)

        self.searchBtn = tk.Button(self.frame, bg='#CFDFEF', text='Search', font=('Arial', 16), command=self.search)
        self.backBtn = tk.Button(self.frame, bg='#CFDFEF', text='Go Back', font=('Arial', 16), command=self.goBack, width=8)
        self.favoriteBtn = tk.Button(self.frame, bg='#CFDFEF', text='Add/Delete Author to Favorites', font=('Arial', 16), command=self.favoriteAuthor, width=30)
        self.seeReviewsBtn = tk.Button(self.frame, bg='#CFDFEF', text='See Reviews', font=('Arial', 16), command=self.viewReviews, width=10)
        self.reviewBtn = tk.Button(self.frame, bg='#CFDFEF', text='Review', font=('Arial', 16), command=self.review, width=8)
        self.maxPriceBox = tk.Checkbutton(self.frame, text='Max By Category', variable=self.checkBoxVar, onvalue=1, offvalue=0, command=self.findMaxByCat)

        self.table = ttk.Treeview(self.frame, columns=('ProductID', 'Author','Title', 'Description', 'Category', 'Price', 'DateInserted'), show='headings')
        self.verticalScroll = ttk.Scrollbar(self.frame, orient='vertical',command=self.table.yview)
        self.horizontalScroll = ttk.Scrollbar(self.frame, orient='horizontal', command=self.table.xview)
        self.table.configure(yscrollcommand=self.verticalScroll.set)
        self.table.configure(xscrollcommand=self.horizontalScroll.set)

        self.table.column('ProductID', width=85)
        self.table.column('Author', width=85)
        self.table.column('Title', width=85)
        self.table.column('Description', width=85)
        self.table.column('Category', width=85)
        self.table.column('Price', width=85)
        self.table.column('DateInserted', width=85)
        self.table.heading('ProductID', text='Product ID')
        self.table.heading('Author', text = 'Author')
        self.table.heading('Title', text='Title')
        self.table.heading('Description', text='Description')
        self.table.heading('Category', text='Category')
        self.table.heading('Price', text='Price')
        self.table.heading('DateInserted', text='Date Inserted')
        self.loadTableData()
    pass

    def formatWidgets(self):
        self.searchText.grid(row=0, column=0, columnspan=1, sticky='news', pady=10)
        self.searchEntry.grid(row=0, column=1, columnspan=1, sticky='news', pady=10)
        self.searchBtn.grid(row=0, column=2, columnspan=1, sticky='news', pady=10)
        self.maxPriceBox.grid(row=1, column=0, columnspan=1, sticky='news', pady=10, padx=10)

        self.table.grid(row=2, column=0, columnspan=4, sticky='news', pady=10)
        self.verticalScroll.grid(row=2, column=4, sticky='ns')
        self.horizontalScroll.grid(row=3, column=0, columnspan=4, sticky='we')

        self.backBtn.grid(row=4, column=0, columnspan=1, sticky='w', pady=10, padx=10)
        self.favoriteBtn.grid(row=4, column=1, columnspan=1, sticky='', pady=10, padx=10)
        self.seeReviewsBtn.grid(row=4, column=2, columnspan=1, pady=10, padx=10)
        self.reviewBtn.grid(row=4, column=3, columnspan=1, sticky='e', pady=10, padx=10) #sticky='we',


        self.frame.pack()
    pass

    def loadTableData(self):
        allItems = self.db.loadItemData()
        counter = 0
        for item in allItems:
            self.table.insert(parent='', index=counter, values=(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
            counter = counter + 1
    pass

    def search(self):
        self.clearTable()
        self.checkBoxVar.set(0)
        self.category = self.catSearch.get()
        self.searchTableData(self.category)
    pass

    def findMaxByCat(self):
        self.clearTable()
        #category = self.catSearch.get()
        if self.checkBoxVar.get() == 1:
            self.displayMaxByCategory(self.category)
        else:
            self.searchTableData(self.category)
    pass

    def searchTableData(self, category):
        searchItems = self.db.searchByCategory(category)
        print(searchItems)
        if searchItems != None:
            counter = 0
            for item in searchItems:
                self.table.insert(parent='', index=counter, values=(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
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

    def displayMaxByCategory(self, category):
        print('in search gui max')
        maxItems = self.db.mostExpensiveByCategory(category)
        if maxItems != None:
            counter = 0
            for item in maxItems:
                self.table.insert(parent='', index=counter, values=(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
                counter = counter + 1
    pass

    def favoriteAuthor(self):

        selectedUser = self.userName
        selectedItem = self.table.focus()
        favoritedAuthor = []
        try:
            if selectedItem:
                row = self.table.item(selectedItem)
                favoritedAuthor = row.get("values")[1]
                if favoritedAuthor != selectedUser:
                    #print(favoritedAuthor + selectedUser)
                    self.db.addToFavoritesTable(selectedUser, favoritedAuthor)
                    self.error('You favorited the person')
                else:
                    self.error('You can\'t favorite yourself')
            else:
                    self.error('No product was selected. \nPlease select a product to favorite author.')
        except mysql.connector.errors.DatabaseError:
            self.db.deleteFromFavoritesTable(selectedUser, favoritedAuthor)
            self.error('You unfavorited the person')
    pass

pass