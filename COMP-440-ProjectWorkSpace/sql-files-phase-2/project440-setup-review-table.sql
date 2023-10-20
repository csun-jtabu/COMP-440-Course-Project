USE project440db;
CREATE TABLE review(
	productid INT,
    user_reviewed VARCHAR(15),
    rating VARCHAR(15),
    description VARCHAR(255),
    date_reviewed DATE,
    FOREIGN KEY(productid) REFERENCES item(productid),
    FOREIGN KEY(user_reviewed) REFERENCES user(username)
);