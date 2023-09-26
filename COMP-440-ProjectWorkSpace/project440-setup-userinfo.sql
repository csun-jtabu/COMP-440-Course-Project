USE project440db;
CREATE TABLE userinfo(
	username VARCHAR(15) NOT NULL PRIMARY KEY,
    password VARCHAR(16) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR(254) NOT NULL UNIQUE
);