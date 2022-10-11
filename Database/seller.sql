use ecommerce_platform;

CREATE TABLE seller (
ID int(10) NOT NULL unique auto_increment,
shop_name varchar(30) NOT NULL,
username varchar(35) NOT NULL,
email varchar(35) NOT NULL,
password varchar(25) NOT NULL,
mobile_no bigint(10) NOT NULL,
GST_NO bigint(15) NOT NULL unique,
primary key (email)
);

INSERT INTO seller VALUES (1,'ABC','Sammed Singalkar','sammedsingalkar@gmail.com','sammed@8308497059','8308497059','0123456789012345');
INSERT INTO seller VALUES (2,'XYZ','Yash Singalkar','yashsingalkar@gmail.com','iamyash@23','8805684639','0147258369014725');
INSERT INTO seller VALUES (3,'LMN','Chinmay Vijapure','chinmay@gmail.com','iamchinmay@47','7588374290','3692581477894');

select * from seller;
drop table seller;