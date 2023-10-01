import tkinter as tk

import DatabaseControl
import ErrorBoxGUI
import LoginPageGUI

class SignUpPageGUI:

    def __init__(self):
        self.db = DatabaseControl.DatabaseControl()
        self.signUpPage = tk.Tk()
        self.signUpPage.geometry('800x500')
        self.signUpPage.title('Sign Up')  # set the name of the window
        self.createWidgets()
        self.formatWidgets()
        self.signUpPage.mainloop()
    pass

    def createWidgets(self):

        self.userNameVar = tk.StringVar()
        self.passwordVar = tk.StringVar()
        self.passwordConfVar = tk.StringVar()
        self.firstNameVar = tk.StringVar()
        self.lastNameVar = tk.StringVar()
        self.emailVar = tk.StringVar()

        self.frame = tk.Frame()  # frame holds all the widgets in the page

        self.instructText = tk.Label(self.frame, text='Please Fill out your Info!', font=('Arial', 30))
        self.userText = tk.Label(self.frame, text='Username: ', font=('Arial', 16))
        self.passwordText = tk.Label(self.frame, text='Password: ', font=('Arial', 16))
        self.passwordConfText = tk.Label(self.frame, text='Confirm Password: ', font=('Arial', 16))
        self.firstNameText = tk.Label(self.frame, text='First Name: ', font=('Arial', 16))
        self.lastNameText = tk.Label(self.frame, text='Last Name: ', font=('Arial', 16))
        self.emailText = tk.Label(self.frame, text='Email: ', font=('Arial', 16))

        self.userEntry = tk.Entry(self.frame, textvariable=self.userNameVar, font=('Arial', 16), width=30)
        self.passwordEntry = tk.Entry(self.frame, textvariable=self.passwordVar, font=('Arial', 16), show='*', width=30)
        self.passwordConfEntry = tk.Entry(self.frame, textvariable=self.passwordConfVar, font=('Arial', 16), show='*', width=30)
        self.firstNameEntry = tk.Entry(self.frame, textvariable=self.firstNameVar, font=('Arial', 16), width=30)
        self.lastNameEntry = tk.Entry(self.frame, textvariable=self.lastNameVar, font=('Arial', 16), width=30)
        self.emailEntry = tk.Entry(self.frame, textvariable=self.emailVar, font=('Arial', 16),width=30)

        self.signUpBtn = tk.Button(self.frame, bg='#CFDFEF', text='Sign-Up', font=('Arial', 16), command=self.submitInfo)
    pass

    def formatWidgets(self):
        self.instructText.grid(row=0, column=1, columnspan=3, sticky='news', pady=40)
        self.userText.grid(row=1, column=0)
        self.passwordText.grid(row=2, column=0)
        self.passwordConfText.grid(row=3, column=0)
        self.firstNameText.grid(row=4, column=0)
        self.lastNameText.grid(row=5, column=0)
        self.emailText.grid(row=6, column=0)

        self.userEntry.grid(row=1, column=1, pady=10)
        self.passwordEntry.grid(row=2, column=1, pady=10)
        self.passwordConfEntry.grid(row=3, column=1, pady=10)
        self.firstNameEntry.grid(row=4, column=1, pady=10)
        self.lastNameEntry.grid(row=5, column=1, pady=10)
        self.emailEntry.grid(row=6, column=1, pady=10)

        self.signUpBtn.grid(row=7, column=2, sticky=tk.S + tk.W, pady=30)

        self.frame.pack()
    pass

    def submitInfo(self):
        key = self.db.signup(self.userNameVar.get(), self.passwordVar.get(), self.passwordConfVar.get(),
                             self.firstNameVar.get(), self.lastNameVar.get(), self.emailVar.get())
        if (key == True):
            self.signUpPage.destroy()
            login = LoginPageGUI.LoginPageGUI()
        else:
            error = ErrorBoxGUI.ErrorBoxGUI('Failed to Sign Up')
    pass