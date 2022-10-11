use ecommerce_platform;

CREATE TABLE payment (srno int(15) NOT NULL AUTO_INCREMENT,
email varchar(35) NOT NULL,
card_holder varchar(20) NOT NULL, 
card_number bigint(16) NOT NULL unique,
expiry date NOT NULL,
company varchar(10) NOT NULL,
primary key (srno)
);

INSERT INTO payment VALUES (1,'sammedsingalkar@gmail.com','Sammed Singalkar','7895014795103698','2022-08-25','visa');
INSERT INTO payment VALUES (2,'sammedsingalkar@gmail.com','Sammed Singalkar','7895014795103699','2022-08-25','mastercard');
INSERT INTO payment VALUES (3,'yashsingalkar@gmail.com','Yash Singalkar','9630741025897412','2022-07-25','visa');

drop table payment;

select * from payment;