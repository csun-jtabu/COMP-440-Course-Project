CREATE DEFINER=`root`@`localhost` PROCEDURE `reset_tables`()
BEGIN
	DROP TABLE IF EXISTS favorite;
	DROP TABLE IF EXISTS review;
	DROP TABLE IF EXISTS item;
    DROP TABLE IF EXISTS user;
    CREATE TABLE user(
		username VARCHAR(15) NOT NULL PRIMARY KEY UNIQUE,
		password VARCHAR(16) NOT NULL,
		firstName VARCHAR(50) NOT NULL,
		lastName VARCHAR(50) NOT NULL,
		email VARCHAR(254) NOT NULL UNIQUE);
    INSERT INTO user (username, password, firstName, lastName, email)
	VALUES 
		('jaz', 'test', 'Jaztin', 'Tabunda', 'jaztin@my.csun.edu'),
		('adr', 'test', 'Adrienne', 'Loaiza', 'adrienne@my.csun.edu'),
		('yan', 'test', 'Yana', 'Zaynullina', 'yana@my.csun.edu'),
		('mah', 'test', 'Mahdi', 'Ebrahimi', 'mahdi@my.csun.edu'),
		('test1', 'test', 'test', 'test', 'test1@my.csun.edu');
	CREATE TABLE item(
		productid INT NOT NULL UNIQUE AUTO_INCREMENT,
		user_inserted varChar(15),
		title varChar(50),
		description varChar(255),
		category varChar(255),
		price INT,
		date_inserted DATE,
		PRIMARY KEY(productid),
		FOREIGN KEY(user_inserted) REFERENCES user(username));
	ALTER TABLE item AUTO_INCREMENT = 1;
	INSERT INTO item(productid, user_inserted, title, description, category, price, date_inserted) 
    VALUES
		(DEFAULT,'jaz','Smartphone','This is the new iPhone X','electronic, cellphone, apple',1000,CURDATE()),
		(DEFAULT,'adr','Laptop','This is the new Mac','electronic, computer, apple',1500,CURDATE()),
		(DEFAULT,'yan','Tablet','This is the new iPad','electronic, Tablet, apple',1100,CURDATE()),
		(DEFAULT,'mah','Smartphone','This is the new Galaxy S23','electronic, cellphone, samsung',800,CURDATE()),
		(DEFAULT,'test1','Tablet','This is the new Galaxy Tab S9','electronic, Tablet, samsung',1000,CURDATE());
	CREATE TABLE review(
		productid INT,
		user_reviewed VARCHAR(15),
		rating VARCHAR(15),
		description VARCHAR(255),
		date_reviewed DATE,
		FOREIGN KEY(productid) REFERENCES item(productid),
		FOREIGN KEY(user_reviewed) REFERENCES user(username));
	INSERT INTO review(productid, user_reviewed, rating, description, date_reviewed) 
    VALUES
		(1, 'adr', 'Excellent', 'cool phone', CURDATE()),
		(2, 'jaz', 'Good', 'cool tablet', CURDATE()),
		(3, 'test1', 'Fair', 'ok laptop', CURDATE()),
		(4, 'yan', 'Poor', 'bad phone', CURDATE()),
		(5, 'mah', 'Fair', 'ok tablet', CURDATE());
	CREATE TABLE favorite(
		username VARCHAR(15),
		favorited_user VARCHAR(15),
		FOREIGN KEY(username) REFERENCES user(username),
		FOREIGN KEY(favorited_user) REFERENCES user(username),
        PRIMARY KEY(username, favorited_user));
	INSERT INTO favorite(username, favorited_user) 
    VALUES
		('jaz', 'yan'),
		('yan', 'adr'),
		('adr', 'mah'),
		('mah', 'test1'),
		('test1', 'jaz');
END