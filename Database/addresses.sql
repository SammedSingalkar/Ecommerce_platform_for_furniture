use ecommerce_platform;

CREATE TABLE addresses (srno int(15) NOT NULL AUTO_INCREMENT,
name varchar(35) NOT NULL,
mobile_number bigint(10) Not NULL,
pincode int(6) NOT NULL,
state varchar(30) NOT NULL,
email varchar(35) NOT NULL,
Landmark text NOT NULL,
city varchar(40) NOT NULL,
primary key (srno)
);

INSERT INTO addresses VALUES (1,'Sammed Singalkar','8308497059','443204','Maharahtra','sammedsingalkar@gmail.com','Ahinsa Marg','Deulgaon Raja');
INSERT INTO addresses VALUES (2,'Yash Singalkar','8805684639','430001','Maharahtra','yashsingalkar@gmail.com','Cidco mahanagar 1, orange pride','Aurangabad');
INSERT INTO addresses VALUES (3,'Yash Singalkar','8805684639','430001','Maharahtra','sammedsingalkar@gmail.com','Cidco mahanagar 1, orange pride','Aurangabad');
select * from addresses;
