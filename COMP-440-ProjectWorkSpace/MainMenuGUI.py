import tkinter as tk
import LoginPageGUI
import SearchGUI
import DatabaseControl
import InsertGUI
from GUIsPhase3 import Phase_3_Part_2GUI
from GUIsPhase3 import Phase_3_Part_3GUI
from GUIsPhase3 import Phase_3_Part_4GUI
from GUIsPhase3 import Phase_3_Part_5GUI

class MainMenuGUI:

    def __init__(self, userName, password):
        self.db = DatabaseControl.DatabaseControl()
        self.userName = userName
        self.password = password
        self.menuPage = tk.Tk()
        self.menuPage.geometry('800x500')
        self.menuPage.title('Main Menu')  # set the name of the window
        self.createWidgets()
        self.formatWidgets()
        self.menuPage.mainloop()
    pass

    def createWidgets(self):
        self.ty = 'Thank you ' + self.userName
        self.frame = tk.Frame()  # frame holds all the widgets in the page
        self.instructText = tk.Label(self.frame, text='You Logged In!', font=('Arial', 30))
        self.tyText = tk.Label(self.frame, text=self.ty, font=('Arial', 30))

        #phase 2 buttons
        self.insertBtn = tk.Button(self.frame, bg='#CFDFEF', text='Insert', font=('Arial', 16), command=self.insert)
        self.searchBtn = tk.Button(self.frame, bg='#CFDFEF', text='Search', font=('Arial', 16), command=self.search)
        self.initializeBtn = tk.Button(self.frame, bg='#CFDFEF', text='Initialize\nDatabase',
                                       font=('Arial', 16), command=self.initializeDB)
        self.logoutBtn = tk.Button(self.frame, bg='#F7CEE2', text='Log Out', font=('Arial', 16), command=self.logout)

        #phase 3 buttons
        self.part2Btn = tk.Button(self.frame, bg='#CFDFEF', text='Phase-3-2', font=('Arial', 16), command=self.phase3Part2)
        self.part3Btn = tk.Button(self.frame, bg='#CFDFEF', text='Phase-3-3', font=('Arial', 16), command=self.phase3Part3)
        self.part4Btn = tk.Button(self.frame, bg='#CFDFEF', text='Phase-3-4', font=('Arial', 16), command=self.phase3Part4)
        self.part5Btn = tk.Button(self.frame, bg='#CFDFEF', text='Phase-3-5', font=('Arial', 16), command=self.phase3Part5)
        self.part6Btn = tk.Button(self.frame, bg='#CFDFEF', text='Phase-3-6', font=('Arial', 16), command=self.phase3Part2)
        self.part7Btn = tk.Button(self.frame, bg='#CFDFEF', text='Phase-3-7', font=('Arial', 16), command=self.phase3Part2)
        self.part8Btn = tk.Button(self.frame, bg='#CFDFEF', text='Phase-3-8', font=('Arial', 16), command=self.phase3Part2)
        self.part9Btn = tk.Button(self.frame, bg='#CFDFEF', text='Phase-3-9', font=('Arial', 16), command=self.phase3Part2)
        self.part10Btn = tk.Button(self.frame, bg='#CFDFEF', text='Phase-3-10', font=('Arial', 16), command=self.phase3Part2)

    pass

    def formatWidgets(self):
        self.instructText.grid(row=0, column=1, columnspan=2, sticky='news', pady=10)
        self.tyText.grid(row=1, column=1, columnspan=2, sticky='news', pady=10)
        self.insertBtn.grid(row=2, column=1, columnspan=1, sticky='news', pady=10)
        self.searchBtn.grid(row=2, column=2, columnspan=1, sticky='news', pady=10)
        self.initializeBtn.grid(row=3, column=1, columnspan=1, sticky='news', pady=10)
        self.logoutBtn.grid(row=3, column=2, columnspan=1, sticky='news', pady=10)
        self.part2Btn.grid(row=4, column=0, columnspan=1, sticky='news', pady=10)
        self.part3Btn.grid(row=4, column=1, columnspan=1, sticky='news', pady=10)
        self.part4Btn.grid(row=4, column=2, columnspan=1, sticky='news', pady=10)
        self.part5Btn.grid(row=4, column=3, columnspan=1, sticky='news', pady=10)
        self.part6Btn.grid(row=5, column=0, columnspan=1, sticky='news', pady=10)
        self.part7Btn.grid(row=5, column=1, columnspan=1, sticky='news', pady=10)
        self.part8Btn.grid(row=5, column=2, columnspan=1, sticky='news', pady=10)
        self.part9Btn.grid(row=5, column=3, columnspan=1, sticky='news', pady=10)
        self.part10Btn.grid(row=6, column=1, columnspan=2, sticky='news', pady=10)

        self.frame.pack()
    pass

    def search(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.menuPage.destroy()
        search = SearchGUI.SearchGUI(self.userName, self.password)
    pass

    def initializeDB(self):
        #successMessage = ErrorBoxGUI.ErrorBoxGUI('Success!\nDatabase Re-Initialized.\nRestarting Program.')
        self.db.dbInitialization()
        #newMenu = self.__init__(self.userName, self.password)
    pass

    def insert(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.menuPage.destroy()
        insert = InsertGUI.InsertGUI(self.userName, self.password)
    pass

    def logout(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.menuPage.destroy()
        login = LoginPageGUI.LoginPageGUI()
    pass

    def phase3Part2(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.menuPage.destroy()
        part2 = Phase_3_Part_2GUI.Phase_3_Part2(self.userName, self.password)
    pass

    def phase3Part3(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.menuPage.destroy()
        part3 = Phase_3_Part_3GUI.Phase_3_Part3(self.userName, self.password)
    pass

    def phase3Part4(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.menuPage.destroy()
        part4 = Phase_3_Part_4GUI.Phase_3_Part4(self.userName, self.password)
    pass

    def phase3Part5(self):
        self.db.myCursor.close()
        self.db.db.close()
        self.menuPage.destroy()
        part4 = Phase_3_Part_5GUI.Phase_3_Part5(self.userName, self.password)
    pass