use ecommerce_platform;

CREATE TABLE orders (order_no int(15) NOT NULL AUTO_INCREMENT,
srno int(15) NOT NULL,
email varchar(35) NOT NULL,
product_name text NOT NULL,
order_date date NOT NULL,
status varchar(20) NOT NULL,
amount int(8) NOT NULL,
quantity int(4) NOT NULL,
payment_method varchar(20) NOT NULL,
primary key (order_no),
foreign key(srno)references product(srno)
);

INSERT INTO orders VALUES (1,1,'sammedsingalkar@gmail.com','Home Centre Emily Fabric 5 Seater Sectional Sofa Set (Beige)','2022-08-25','completed',50000,3,'upi');
INSERT INTO orders VALUES (2,1,'sammedsingalkar@gmail.com','Home Centre Emily Fabric 5 Seater Sectional Sofa Set (Beige)','2022-07-25','completed',50000,3,'cod');

select * from orders;
drop table orders;

