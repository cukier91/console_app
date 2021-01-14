CREATE TABLE Users(id serial PRIMARY KEY,
name varchar(60), email varchar(60) UNIQUE, password varchar(60));

CREATE TABLE Messages(id serial PRIMARY KEY, user_id int, message text,
 FOREIGN KEY(user_id) REFERENCES Users(id));

CREATE TABLE Items(id serial PRIMARY KEY, name varchar(40), description text, price decimal(7,2));

CREATE TABLE Orders(id serial PRIMARY KEY, description text);

CREATE TABLE ItemOrders(ItemOrders_id serial PRIMARY KEY, item_id int NOT NULL, order_id int NOT NULL,
FOREIGN KEY(item_id) REFERENCES Items(id),
FOREIGN KEY(order_id) REFERENCES Orders(id));

SELECT * from Items Where price > 13;

INSERT INTO Orders(description)
VALUES('Bardzo fajne stare krzesło');

INSERT INTO Users(name)
VALUES('Waldemar');

DELETE From Users WHERE id=7;

SELECT * from Users JOIN Messages
ON Users.id = Messages.user_id
Where Messages.user_id >0;



