use ecommerce_platform;

CREATE TABLE contact (
name varchar(35) NOT NULL,
email varchar(35) NOT NULL,
subject varchar(200) NOT NULL,
message text NOT NULL,
primary key (email)
);

INSERT INTO user VALUES ('Sammed Singalkar','sammedsingalkar@gmail.com','Regarding technical issue','Hello i am sam there is an problem in my account plz resolve');
INSERT INTO user VALUES ('Yash Singalkar','yashsingalkar@gmail.com','Issue','hello i am sammed');