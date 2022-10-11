use ecommerce_platform;

CREATE TABLE user (
name varchar(35) NOT NULL unique,
email varchar(35) NOT NULL,
password varchar(25) NOT NULL,
mobile_no bigint(10) NOT NULL,
membership varchar(25) NOT NULL,
primary key (email)
);

INSERT INTO user VALUES ('Sammed Singalkar','sammedsingalkar@gmail.com','sammed@8308497059','8308497059','YES');
INSERT INTO user VALUES ('Yash Singalkar','yashsingalkar@gmail.com','iamyash@23','8805684639','NO');
INSERT INTO user VALUES ('Chinmay Vijapure','chinmay@gmail.com','iamchinmay@47','7588374290','NO');


select * from user;
drop table user;