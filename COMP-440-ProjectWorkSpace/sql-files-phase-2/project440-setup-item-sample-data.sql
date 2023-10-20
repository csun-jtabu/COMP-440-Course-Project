USE project440db;
ALTER TABLE item AUTO_INCREMENT = 1;
INSERT INTO item(productid, user_inserted, title, description, category, price, date_inserted) VALUES
	(DEFAULT,'jaz','Smartphone','This is the new iPhone X','electronic, cellphone, apple',1000,'2023-10-19'),
    (DEFAULT,'jaz','Laptop','This is the new Mac','electronic, computer, apple',1500,'2023-10-19'),
    (DEFAULT,'jaz','Tablet','This is the new iPad','electronic, Tablet, apple',1100,'2023-10-19');