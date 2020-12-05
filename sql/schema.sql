CREATE TABLE users(
	username VARCHAR(15) NOT NULL,
	firstname VARCHAR(20),
	lastname VARCHAR(20),
	email VARCHAR(50),
	proffilename VARCHAR(100),
	password VARCHAR(512) NOT NULL,
	PRIMARY KEY(username)
);