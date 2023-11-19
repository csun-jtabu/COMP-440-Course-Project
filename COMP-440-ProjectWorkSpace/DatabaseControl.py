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
            'FROM user;')
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
        sqlStatement = "SELECT * FROM user WHERE username = %s;"
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
        sqlStatement = "SELECT * FROM user WHERE email = %s;"
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
        sqlStatement = "SELECT * FROM user WHERE username = %s;"
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
        sqlString = category + ',|, ' + category + '$|^' + category + '$'
        sqlStatement = ("SELECT productid, title, description, category, price FROM item "
                        "WHERE category REGEXP %s;")
        self.myCursor.execute(sqlStatement, (sqlString,))
        searchedItems = self.myCursor.fetchall()
        return searchedItems
    pass

    def mostExpensiveByCategory(self, category):
        searchedItems = self.searchByCategory(category)
        if searchedItems != []:
            mostExpensive = [searchedItems[0]]
            for item in searchedItems:
                print(mostExpensive)
                if mostExpensive[0][4] < item[4]:
                    mostExpensive.clear()
                    mostExpensive = [item]
                elif (mostExpensive[0][4] == item[4]) and (item not in mostExpensive):
                    mostExpensive.append(item)

            return mostExpensive
        else:
            return None
    pass

    def displayProduct(self, productId):
        sqlStatement = "SELECT * FROM item WHERE productid = %s;"
        self.myCursor.execute(sqlStatement, (productId,))
        currentProduct = self.myCursor.fetchone()
        return currentProduct
    pass

    def submitReview(self, productId, userName, rating, description):
        self.myCursor.callproc('write_review', (productId, userName, rating, description))
        self.db.commit()
    pass

    def loadReviewData(self, productId):
        sqlStatement = "SELECT user_reviewed, rating, description FROM review WHERE productid = %s;"
        self.myCursor.execute(sqlStatement, (productId,))
        allItems = self.myCursor.fetchall()
        return allItems
    pass

    def dbInitialization(self):
        #print('Gone to MYSQL')
        self.myCursor.callproc('reset_tables_except_user') #test / reset_tables_except_user
        #print('Back on Python')
        self.db.commit()
    pass

    def insertItem(self, userName, title, description, category, price):
        self.myCursor.callproc('insert_item_procedure', (userName, title, description, category, price))
        self.db.commit()
    pass

    # this will ensure that there will be only one review per product for each member
    def checkNumUserReview(self, userName, productId):
        sqlStatement = "SELECT count(*) FROM review WHERE user_reviewed = %s AND productid = %s;"
        self.myCursor.execute(sqlStatement, (userName, productId))
        numUserReviews = self.myCursor.fetchone()
        if(numUserReviews[0] < 1):
            return True
        else:
            return False
    pass

    def checkSelfReview(self, userName, productId):
        sqlStatement = "SELECT count(*) FROM item WHERE productid = %s AND user_inserted = %s;"
        self.myCursor.execute(sqlStatement, (productId, userName))
        selfReviews = self.myCursor.fetchone()
        if(selfReviews[0] == 0):
            return True
        else:
            return False
    pass

    def phase3Part2(self, cat1, cat2):
        sqlString1 = cat1 + ',|, ' + cat1 + '$|^' + cat1 + '$'
        sqlString2 = cat2 + ',|, ' + cat2 + '$|^' + cat2 + '$'
        sqlStatement = ("SELECT user_inserted, date_inserted "
                        "FROM item "
                        "WHERE (category REGEXP %s) AND NOT (category REGEXP %s) "
                        "GROUP BY date_inserted, user_inserted;")
        self.myCursor.execute(sqlStatement, (sqlString1, sqlString2,))
        cat1UserList = self.myCursor.fetchall()
        sqlStatement = ("SELECT user_inserted, date_inserted "
                        "FROM item "
                        "WHERE (category REGEXP %s) AND NOT (category REGEXP %s) "
                        "GROUP BY date_inserted, user_inserted;")
        self.myCursor.execute(sqlStatement, (sqlString2, sqlString1,))
        cat2UserList = self.myCursor.fetchall()
        finalUsers = self.checkLists(cat1UserList, cat2UserList)
        finalUsers = self.getUserInfoTemplate(finalUsers)
        return finalUsers
    pass

    # this method will compare two lists and return a list of common elements
    # we need this for phase 3
    def checkLists(self, List1, List2):
        newList = []
        if (List1 != []) and (List1 != []):
            for element in List1:
                if element in List2:
                    newList.append(element)
        return newList
    pass

    # so we can output data onto userTableGUITemplate properly
    def getUserInfoTemplate(self, userList):
        newList = []
        sqlStatement = ("SELECT * "
                        "FROM user "
                        "WHERE username = %s;")
        if userList != []:
            for element in userList:
                self.myCursor.execute(sqlStatement, (element[0],))
                newElement = self.myCursor.fetchone()
                newList.append(newElement)
        return newList
    pass