USE project440db;
CREATE TABLE item(
	productid INT NOT NULL UNIQUE AUTO_INCREMENT,
    user_inserted varChar(15),
    title varChar(50),
    description varChar(255),
    category varChar(255),
    price INT,
    date_inserted DATE,
    PRIMARY KEY(productid),
    FOREIGN KEY(user_inserted) REFERENCES user(username)
);

