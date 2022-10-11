use ecommerce_platform;

CREATE TABLE seller_orders (order_no int(15) NOT NULL AUTO_INCREMENT,
srno int(15) NOT NULL,
email varchar(35) NOT NULL,
user_email varchar(35) NOT NULL,
product_name text NOT NULL,
order_date date NOT NULL,
status varchar(20) NOT NULL,
amount int(8) NOT NULL,
quantity int(4) NOT NULL,
primary key (order_no),
foreign key(srno)references product(srno),
foreign key(user_email)references user(email)
);

INSERT INTO seller_orders VALUES (1,1,'sammedsingalkar@gmail.com','sammedsingalkar@gmail.com','Home Centre Emily Fabric 5 Seater Sectional Sofa Set (Beige)','2022-08-25','Approved',50000,3);
INSERT INTO seller_orders VALUES (2,1,'sammedsingalkar@gmail.com','yashsingalkar@gmail.com','Home Centre Emily Fabric 5 Seater Sectional Sofa Set (Beige)','2022-07-25','Pending',50000,3);
INSERT INTO seller_orders VALUES (3,1,'sammedsingalkar@gmail.com','sammedsingalkar@gmail.com','Home Centre Emily Fabric 5 Seater Sectional Sofa Set (Beige)','2022-07-25','Pending',50000,3);
INSERT INTO seller_orders VALUES (4,1,'sammedsingalkar@gmail.com','yashsingalkar@gmail.com','Home Centre Emily Fabric 5 Seater Sectional Sofa Set (Beige)','2022-07-25','Pending',50000,3);

select * from seller_orders;

drop table seller_orders;