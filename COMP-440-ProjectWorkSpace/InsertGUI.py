import tkinter as tk
import DatabaseControl
import MainMenuGUI

class InsertGUI:
    def __init__(self, userName, password):

        self.userName = userName
        self.password = password
        self.db = DatabaseControl.DatabaseControl()
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Item Insertion")
        self.createWidgets()
        self.formatWidgets()
        self.root.mainloop()

    def createWidgets(self):
        self.titleVar = tk.StringVar()
        self.descriptionVar = tk.StringVar()
        self.categoryVar = tk.StringVar() #self.root
        self.priceVar = tk.StringVar()

        self.title_label = tk.Label(self.root, text="Title:")
        self.title_entry = tk.Entry(self.root, width=40, textvariable=self.titleVar)

        self.description_label = tk.Label(self.root, text="Description:")
        self.description_entry = tk.Entry(self.root, width=40, textvariable=self.descriptionVar)

        self.category_label = tk.Label(self.root, text="Category:")
        self.categories = ["Electronics", "Clothing", "Furniture", "Books", "Other"]

        self.categoryVar.set(self.categories[0])

        self.category_dropdown = tk.OptionMenu(self.root, self.categoryVar, *self.categories)

        self.price_label = tk.Label(self.root, text="Price:")
        self.price_entry = tk.Entry(self.root, width=40, textvariable=self.priceVar)
        # Create a button to submit the item
        self.submit_button = tk.Button(self.root, text="Submit", command=self.insert_item)
        self.back_button = tk.Button(self.root, text="Back", command=self.goBack)
    pass

    def formatWidgets(self):
        self.title_label.grid(row=0, column=0, padx=10, pady=5)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)
        self.description_label.grid(row=1, column=0, padx=10, pady=5)
        self.description_entry.grid(row=1, column=1, padx=10, pady=5)
        self.category_label.grid(row=2, column=0, padx=10, pady=5)
        self.category_dropdown.grid(row=2, column=1, padx=10, pady=5)
        self.price_label.grid(row=3, column=0, padx=10, pady=5)
        self.price_entry.grid(row=3, column=1, padx=10, pady=5)
        self.submit_button.grid(row=4, columnspan=2, padx=10, pady=10)
        self.back_button.grid(row=4, columnspan=1, padx=10, pady=10)
    pass

    def insert_item(self):
        self.db.insertItem(self.userName.get(), self.titleVar.get(),
                           self.descriptionVar.get(), self.categoryVar.get(), self.priceVar.get())
    pass

    def goBack(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.root.destroy()
        menu = MainMenuGUI.MainMenuGUI(self.userName, self.password)
    pass

    '''def insert_item(self, title, description, category, price, user_id):
            title = self.title_entry.get()
            description = self.description_entry.get()
            category = self.category_var.get()
            price = self.price_entry.get()
            user_id = 1  # Replace with the user's ID or a way to determine the user ID
            posted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Insert data into the "item" table
            insert_query = "INSERT INTO item (title, description, category, price, user_id, posted_date) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (title, description, category, price, user_id, posted_date)

            try:
                self.myCursor.execute(insert_query, data)
                self.db.commit()
                print("Item added successfully.")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.db.rollback()'''

    '''def run(self):
        self.root.mainloop()'''


    '''if __name__ == "__main__":
        insert_gui = InsertGUI()
        insert_gui.run()'''

'''self.dbPassword = 'yourpassword'  # Replace with your database password

        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password=self.dbPassword,
            port='3306',
            database='project440db'
        )'''