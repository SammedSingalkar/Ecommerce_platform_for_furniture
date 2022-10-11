use ecommerce_platform;

CREATE TABLE teapoy (srno int(10) NOT NULL AUTO_INCREMENT,
model_no int(25) NOT Null, name text Not Null,
brand varchar(25) NOT NULL, Room_type varchar(25),
Product_Dimensions varchar(40),
color varchar(20) NOT NULL, style varchar(25) Not Null, shape varchar(25),
`frame_material` varchar(20) Not null,`top_material` varchar(25),
weight varchar(25),  about text Not Null,
price int(10) NOT NULL,
original_price int(10) NOT NULL,
-- img LONGBLOB NOT NULL, 
primary key (srno)
);

INSERT INTO teapoy VALUES(1,64544777,'Prima 5008 Center Trolley Coffee Table/Tea Table/Teapoy for Home, Office & Outdoor (Weather Brown)','Prima',null,'20.1D x 26W x 26H Centimeters','Weather Brown','Contemporary',null,'Plastic','plastic','2.8kG','Made of 100% Virgin Plastic: Provides the ultimate strength and durability to the product.
Safe and Non-Toxic: Only the highest quality of plastic is used in our products with rigorous safety tests.
High Load Bearing Capacity: Rigorously tested for safety and high-load bearing capacity.
Made in India
Quick and Easy Assembly: Follow a few simple steps provided with the package to assemble and enjoy your product!
Easy to Clean: Simply wipe down with a cloth and it will shine as good as new.
Low Maintenance: Assured elimination of any hassles or stress with Prima products!',1199,1500);

INSERT INTO teapoy VALUES(2,84798788,'BAS Brwon Art Shoppee Fold-able Rectangle Shaped Side Table/Tea Coffee Breakfast and Laptop Table ( Engineered Wood,White)','BAS','Study Room','40.6D x 61W x 50.8H Centimeters','White','Modern','Rectangle','Wood','Engineered Wood',null,'Multi functional: Not Only The Table Has A Very Unique Look But Also The Table Is Multi functional. Can Keep Magazine That Give A Luxury Look This Table Can Be Used For More Than One Purpose Such As Coffee Table, Kids Study Table, Utility Table, Breakfast Table.
This Table Is Very Handy And Requires Less Effort With Assembly. This Design Is Simply Irresistible. Buyer will have to self-assemble the product. We do not pay for any assembly services
Table Colour White Black Brown Gray & Natural Available
Product Dimension : 24 inch x 16 inch x 20 inch and Top Size is 24x16 Inch',1899,2200);

INSERT INTO teapoy VALUES(3,84798788,'BAS Brwon Art Shoppee Fold-able Rectangle Shaped Side Table/Tea Coffee Breakfast and Laptop Table ( Engineered Wood,White)','BAS','Study Room','40.6D x 61W x 50.8H Centimeters','Yellow','Modern','Rectangle','Wood','Engineered Wood',null,'Multi functional: Not Only The Table Has A Very Unique Look But Also The Table Is Multi functional. Can Keep Magazine That Give A Luxury Look This Table Can Be Used For More Than One Purpose Such As Coffee Table, Kids Study Table, Utility Table, Breakfast Table.
This Table Is Very Handy And Requires Less Effort With Assembly. This Design Is Simply Irresistible. Buyer will have to self-assemble the product. We do not pay for any assembly services
Table Colour Yello Black Brown Gray & Natural Available
Product Dimension : 24 inch x 16 inch x 20 inch and Top Size is 24x16 Inch',1899,2200);

INSERT INTO teapoy VALUES(4,84798788,'BAS Brwon Art Shoppee Fold-able Rectangle Shaped Side Table/Tea Coffee Breakfast and Laptop Table ( Engineered Wood,White)','BAS','Study Room','40.6D x 61W x 50.8H Centimeters','Blue','Modern','Rectangle','Wood','Engineered Wood',null,'Multi functional: Not Only The Table Has A Very Unique Look But Also The Table Is Multi functional. Can Keep Magazine That Give A Luxury Look This Table Can Be Used For More Than One Purpose Such As Coffee Table, Kids Study Table, Utility Table, Breakfast Table.
This Table Is Very Handy And Requires Less Effort With Assembly. This Design Is Simply Irresistible. Buyer will have to self-assemble the product. We do not pay for any assembly services
Table Colour Blue Black Brown Gray & Natural Available
Product Dimension : 24 inch x 16 inch x 20 inch and Top Size is 24x16 Inch',1899,2200);





drop table teapoy;
select * from teapoy;
-- dressing table, dinning table, cuboard, chairs, divan, 