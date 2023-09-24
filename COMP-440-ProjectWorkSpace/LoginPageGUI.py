import tkinter as tk

import MainMenuGUI
import SignUpPageGUI


class LoginPageGUI:

    def __init__(self):
        self.loginPage = tk.Tk()
        self.loginPage.geometry('800x500')
        self.loginPage.title('Login Page')  # set the name of the window
        self.createWidgets()
        self.formatWidgets()
        self.loginPage.mainloop()
    pass

    def createWidgets(self):

        self.frame = tk.Frame() #frame holds all the widgets in the page
        self.userNameVar = tk.StringVar() # this holds the username input
        self.passwordVar = tk.StringVar() # this holds the password input

        #text
        self.instructText = tk.Label(self.frame, text='Please Login!', font=('Arial',30))
        self.userText = tk.Label(self.frame, text='Username: ', font=('Arial',16))
        self.passwordText = tk.Label(self.frame, text='Password: ', font=('Arial', 16))

        #interactive items
        self.userEntry = tk.Entry(self.frame, textvariable= self.userNameVar, font=('Arial', 16), width= 30)
        self.passwordEntry = tk.Entry(self.frame, textvariable= self.passwordVar, font=('Arial', 16), show='*', width= 30)
        self.loginBtn = tk.Button(self.frame, bg='#CFDFEF', text= 'Login', font=('Arial', 16), command= self.loggedIn)
        self.signUpBtn = tk.Button(self.frame, bg='#F7CEE2', text= 'Sign Up', font=('Arial', 16), command= self.signUp)
    pass

    def formatWidgets(self):
        self.instructText.grid(row= 0, column= 1, columnspan=3, sticky='news', pady=40)
        self.userText.grid(row= 1, column= 0)
        self.passwordText.grid(row= 2, column= 0)
        self.userEntry.grid(row= 1, column= 1, pady=20)
        self.passwordEntry.grid(row= 2, column= 1, pady=20)
        self.loginBtn.grid(row= 3, column= 1, sticky= tk.S+tk.W, pady=5)
        self.signUpBtn.grid(row= 3, column= 1, sticky= tk.S+tk.E, pady=5)
        self.frame.pack()
    pass

    def loggedIn(self):
        self.loginPage.destroy()
        menu = MainMenuGUI.MainMenuGUI(userName= self.userNameVar, password= self.passwordVar)
    pass

    def signUp(self):
        self.loginPage.destroy()
        signUp = SignUpPageGUI.SignUpPageGUI()
    pass


