CREATE DEFINER=`root`@`localhost` PROCEDURE `reset_tables_except_user`()
BEGIN
	DROP TABLE IF EXISTS review;
	DROP TABLE IF EXISTS item;
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
		(DEFAULT,'jaz','Laptop','This is the new Mac','electronic, computer, apple',1500,CURDATE()),
		(DEFAULT,'jaz','Tablet','This is the new iPad','electronic, Tablet, apple',1100,CURDATE()),
		(DEFAULT,'jaz','Smartphone','This is the new Galaxy S23','electronic, cellphone, samsung',800,CURDATE()),
		(DEFAULT,'jaz','Tablet','This is the new Galaxy Tab S9','electronic, Tablet, samsung',1000,CURDATE());
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
		(1, 'jaz', 'excellent', 'cool phone', CURDATE()),
		(2, 'jaz', 'good', 'cool tablet', CURDATE()),
		(3, 'jaz', 'fair', 'ok laptop', CURDATE()),
		(4, 'jaz', 'poor', 'bad phone', CURDATE()),
		(5, 'jaz', 'fair', 'ok tablet', CURDATE());
END;