import tkinter as tk
import mysql.connector
from datetime import datetime

class InsertGUI:
    def __init__(self):
        self.dbPassword = 'yourpassword'  # Replace with your database password

        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password=self.dbPassword,
            port='3306',
            database='project440db'
        )

        self.cursor = self.db.cursor()

        self.root = tk.Tk()
        self.root.title("Item Insertion")
        self.root.geometry("500x300")

        title_label = tk.Label(self.root, text="Title:")
        title_label.grid(row=0, column=0, padx=10, pady=5)
        self.title_entry = tk.Entry(self.root, width=40)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        description_label = tk.Label(self.root, text="Description:")
        description_label.grid(row=1, column=0, padx=10, pady=5)
        self.description_entry = tk.Entry(self.root, width=40)
        self.description_entry.grid(row=1, column=1, padx=10, pady=5)

        category_label = tk.Label(self.root, text="Category:")
        category_label.grid(row=2, column=0, padx=10, pady=5)
        categories = ["Electronics", "Clothing", "Furniture", "Books", "Other"]
        self.category_var = tk.StringVar(self.root)
        self.category_var.set(categories[0])
        category_dropdown = tk.OptionMenu(self.root, self.category_var, *categories)
        category_dropdown.grid(row=2, column=1, padx=10, pady=5)

        price_label = tk.Label(self.root, text="Price:")
        price_label.grid(row=3, column=0, padx=10, pady=5)
        self.price_entry = tk.Entry(self.root, width=40)
        self.price_entry.grid(row=3, column=1, padx=10, pady=5)

        # Create a button to submit the item
        submit_button = tk.Button(self.root, text="Submit", command=self.insert_item)
        submit_button.grid(row=4, columnspan=2, padx=10, pady=10)

    def insert_item(self):
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
            self.cursor.execute(insert_query, data)
            self.db.commit()
            print("Item added successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.db.rollback()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    insert_gui = InsertGUI()
    insert_gui.run()

