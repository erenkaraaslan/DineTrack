CREATE TABLE users(
	username VARCHAR(15) NOT NULL,
	firstname VARCHAR(20) NOT NULL,
	lastname VARCHAR(20) NOT NULL,
	email VARCHAR(50) NOT NULL,
	proffilename VARCHAR(100) NOT NULL,
	password VARCHAR(512) NOT NULL,
	PRIMARY KEY(username)
);