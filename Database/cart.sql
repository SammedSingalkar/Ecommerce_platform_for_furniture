use ecommerce_platform;

CREATE TABLE cart (srno int(15) NOT NULL AUTO_INCREMENT,
no int(15) NOT NULL,
email varchar(35) NOT NULL,
product_name text NOT NULL,
color varchar(25) NOT NULL,
quantity int(25) NOT NULL,
price int(10) NOT NULL,
primary key (srno),
foreign key(no)references product(srno)
);

INSERT INTO cart VALUES (1,1,'sammedsingalkar@gmail.com','Home Centre Emily Fabric 5 Seater Sectional Sofa Set (Beige)','Beige',2,'32998');
INSERT INTO cart VALUES (2,1,'sammedsingalkar@gmail.com','Home Centre Emily Fabric 5 Seater Sectional Sofa Set (Beige)','Beige',3,'32998');

select * from cart;
SELECT COUNT(srno)
FROM cart where email = 'sammedsingalkar@gmail.com';

drop table cart;