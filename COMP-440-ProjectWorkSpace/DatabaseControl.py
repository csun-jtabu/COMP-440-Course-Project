import mysql.connector

import re


class DatabaseControl:

    def __init__(self):
        # put your own password here---------------
        self.dbPassword = 'DataChimneySQL2'
        # -----------------------------------------

        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password=self.dbPassword,
            port='3306',
            database='project440db'
        )

        # cursor is how we'll be able to execute sql statements in this program
        self.myCursor = self.db.cursor()
    pass

    def loadAllUserData(self):
        # this will get everyone in our user database and their information
        self.myCursor.execute(
            'SELECT * '
            'FROM user')
        # this will save the tuple data results from the query above into a list
        self.users = self.myCursor.fetchall()
    pass

    def printAllUsers(self):
        for user in self.users:
            print('Username: ' + user[0])
            print('Password: ' + user[1])
            print('FirstName: ' + user[2])
            print('LastName: ' + user[3])
            print('Email: ' + user[4])
    pass

    def login(self, userName, password):
        validity = False
        sqlStatement = "SELECT * FROM user WHERE username = %s"
        self.myCursor.execute(sqlStatement, (userName,))
        currentAccount = self.myCursor.fetchone()
        if currentAccount != None:
            if currentAccount[0] == userName and currentAccount[1] == password:
                validity = True
        return validity
    pass

    def signup(self, userName, password, confPass, firstName, lastName, email):
        validatedUser = self.validUserName(userName)
        validatedPass = self.verifyPassword(password, confPass)
        validatedfirstName = self.validName(firstName)
        validatedLastName = self.validName(lastName)
        validatedEmail = self.validEmail(email)
        if (validatedUser and validatedPass and validatedfirstName and validatedLastName and validatedEmail):
            sqlStatment = ("INSERT INTO user VALUES(%s, %s, %s, %s, %s);") #user(username, password, firstName, lastName, email)
            sigupValues = (userName, password, firstName, lastName, email)
            self.myCursor.execute(sqlStatment, sigupValues)
            self.db.commit()
            return True
        else:
            return False
    pass

    def verifyPassword(self, password, confPass):
        validPasswordLength = 16
        if(password == confPass) and (len(password) <= validPasswordLength):
            return True
        else:
            return False
    pass

    def validName(self, name):
        # This pattern is basically saying to find a pattern in which
        # the inserted string starts with a letter (lowercase/uppercase) and ends with a letter
        # and has 1 or more alphabets in between
        validNameLength = 50
        pattern = "^[a-zA-Z]+$"
        answerList = re.search(pattern, name)
        if (answerList != None) and (len(name) <= validNameLength):
            return True
        else:
            return False
    pass

    def validEmail(self, email):
        valid = False
        validEmailLength = 254
        sqlStatement = "SELECT * FROM user WHERE email = %s"
        self.myCursor.execute(sqlStatement, (email,))
        selectedEmail = self.myCursor.fetchone()
        pattern = "^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9_\.\-]+\.[a-zA-Z]{2,7}$"
        answerList = re.search(pattern, email)
        if selectedEmail == None:
            if (answerList != None) and (len(email) <= validEmailLength):
                valid = True
            else:
                valid = False
        return valid
    pass

    def validUserName(self, userName):
        valid = False
        validUserNameLength = 15
        sqlStatement = "SELECT * FROM user WHERE username = %s"
        self.myCursor.execute(sqlStatement, (userName,))
        selectedName = self.myCursor.fetchone()
        if selectedName == None:
            if (len(userName) <= validUserNameLength):
                valid = True
            else:
                valid = False
        return valid
    pass

    def loadItemData(self):
        sqlStatement = "SELECT productid, title, description, category, price FROM item;"
        self.myCursor.execute(sqlStatement)
        allItems = self.myCursor.fetchall()
        return allItems
    pass

    def searchByCategory(self, category):
        sqlStatement = ("SELECT productid, title, description, category, price FROM item "
                        "WHERE category REGEXP %s;")
        self.myCursor.execute(sqlStatement, (category,))
        searchedItems = self.myCursor.fetchall()
        return searchedItems
    pass
