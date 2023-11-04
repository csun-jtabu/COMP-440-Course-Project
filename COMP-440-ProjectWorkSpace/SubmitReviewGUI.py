import DatabaseControl
import tkinter as tk
from tkinter import ttk
from datetime import date

import SearchGUI
import ViewReviewsGUI

class SubmitReviewGUI:
	def __init__(self, userName, password, productId):
		self.userName = userName
		self.password = password
		self.productId = productId
		self.db = DatabaseControl.DatabaseControl()
		self.submitReviewPage = tk.Tk()
		self.submitReviewPage.geometry('1500x520')
		self.submitReviewPage.title('Submit Your Review')
		self.createWidgets()
		self.formatWidgets()
		self.submitReviewPage.mainloop()
	pass

	def createWidgets(self):
		self.frame = tk.Frame()

		self.selectedProductFrame = tk.LabelFrame(self.frame, text="Your Selected Product", font=('Arial', 16))
		self.table = ttk.Treeview(self.selectedProductFrame, columns=('ProductID','Title', 'Description', 'Category', 'Price'), show='headings', height=1)
		self.reviewDetailsFrame = tk.LabelFrame(self.frame, text="Write a Review", font=('Arial', 16))

		self.ratingLabel = tk.Label(self.reviewDetailsFrame, text="Rating", font=('Arial', 16))
		self.descriptionLabel = tk.Label(self.reviewDetailsFrame, text="Description", font=('Arial', 16))
		self.cancelButton = tk.Button(self.reviewDetailsFrame, text="Cancel", bg='#CFDFEF', font=('Arial', 16), command=self.goBack)
		self.submitButton = tk.Button(self.reviewDetailsFrame, text="Submit", bg='#CFDFEF', font=('Arial', 16))
		self.ratingCombobox = ttk.Combobox(self.reviewDetailsFrame, values=["Excellent", "Good", "Fair", "Poor"], font=('Arial', 16))
		self.ratingCombobox.insert(0, "Select a Rating")
		self.descriptionEntry = tk.Text(self.reviewDetailsFrame, width=50, height=4, font=('Arial', 16))

		self.table.heading('ProductID', text='Product ID')
		self.table.heading('Title', text='Title')
		self.table.heading('Description', text='Description')
		self.table.heading('Category', text='Category')
		self.table.heading('Price', text='Price')
		self.displaySelectedProduct()
	pass

	def formatWidgets(self):
		self.selectedProductFrame.grid(row=0, column=0, pady=30)
		self.table.grid(row=0, column=0, sticky='news', padx=60, pady=25)

		self.reviewDetailsFrame.grid(row=1, column=0)
		self.ratingLabel.grid(row=0, column=0, sticky='w', padx=20, pady=30)
		self.ratingCombobox.grid(row=0, column=1, sticky='w', padx=20, pady=10)
		self.descriptionLabel.grid(row=1,column=0, sticky='news', padx=20, pady=30)
		self.descriptionEntry.grid(row=1, column=1, padx=20, pady=10)
		self.cancelButton.grid(row=2, column=0, sticky='w', padx=20, pady=10)
		self.submitButton.grid(row=2, column=1, sticky='e', padx=20, pady=10)

		self.frame.pack()
	pass

	def displaySelectedProduct(self):
		oneProduct = self.db.displayProduct(self.productId)
		#print(oneProduct)
		if oneProduct != None:
			self.table.insert('', 'end', values=(oneProduct[0], oneProduct[2], oneProduct[3], oneProduct[4], oneProduct[5]))
	pass

	'''
	def submit(self):
		today = date.today()
		info = self.db.submitReview(self.productId, self.userName, self.ratingCombobox.get(), self.descriptionEntry.get('1.0', 'end-1c'), today)
		self.submitReviewPage.destroy()
		viewReviews = ViewReviewsGUI.ViewReviewsGUI(self.userName, self.password, self.productId)
	pass
	'''

	def goBack(self):
		self.db.myCursor.close()
		self.db.db.close()
		self.submitReviewPage.destroy()
		search = SearchGUI.SearchGUI(self.userName, self.password)
	pass
pass