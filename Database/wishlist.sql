use ecommerce_platform;

CREATE TABLE wishlist (srno int(15) NOT NULL AUTO_INCREMENT,
no int(15) NOT NULL,
email varchar(35) NOT NULL,
`product_name` varchar(400) NOT NULL,
primary key (srno),
foreign key(no)references product(srno),
foreign key(`product_name`)references product(`name`)
);

INSERT INTO wishlist VALUES (1,1,'sammedsingalkar@gmail.com','Home Centre Emily Fabric 5 Seater Sectional Sofa Set (Beige)');

select * from wishlist;

drop table wishlist;

delete from wishlist where srno = '3'



-- date
-- type forex - couch

drop table wishlist;