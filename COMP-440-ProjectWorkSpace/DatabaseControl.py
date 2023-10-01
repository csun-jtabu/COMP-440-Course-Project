import mysql.connector

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
        sqlStatement = "SELECT * FROM user WHERE username = '{}'".format(userName)
        self.myCursor.execute(sqlStatement)
        currentAccount = self.myCursor.fetchone()
        if currentAccount[0] == userName and currentAccount[1] == password:
            validity = True
        return validity
    pass

    def signup(self, userName, password, confPass, firstName, lastName, email):
        if (password == confPass):
            sqlStatment = ("INSERT INTO user VALUES(%s, %s, %s, %s, %s);") #user(username, password, firstName, lastName, email)
            sigupValues = (userName, password, firstName, lastName, email)
            self.myCursor.execute(sqlStatment, sigupValues)
            self.db.commit()
            return True
        else:
            return False
    pass


