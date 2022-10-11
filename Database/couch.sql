use ecommerce_platform;

CREATE TABLE product (srno int(25) NOT NULL AUTO_INCREMENT,
model_no int(25) NOT Null, `name`varchar(400) NOT NULL unique,
`type` varchar(10), brand varchar(20) NOT NULL, style varchar(25),
Room_type varchar(30),`fabric_type` varchar(25), color varchar(20) NOT NULL,
`seating_capacity` int(10),
shape varchar(10),
`frame_material` varchar(20),
`speacial_feature` varchar(30),
about text NOT NULL,
typed varchar(25) NOT NULL,
price int(10) NOT NULL,
original_price int(10) NOT NULL,
seller_id int(11) NOT NULL,
-- `image` text COLLATE utf8mb4_unicode_ci NOT NULL,
primary key (srno)
)
ENGINE = InnoDB;


INSERT INTO product VALUES (1,548679874,'Home Centre Emily Fabric 5 Seater Sectional Sofa Set (Beige)','Sectional','Home Centre','3+2 Seater','Living Room','Polyster','Beige',5,'3+2',null,null,'Product Dimensions: Length (184 cm), Width (92 cm), Height (88 cm)
Primary Material: Fabric, Upholstery Material: Polyester
Color: Beige, Style: Contemporary
Seating Capacity: Five Seat
Assembly Required: The product requires carpenter assembly and will be provided by the seller
Warranty: 1 year on product
Three seater sofa: Length (184 cm), Width (92 cm), Height (88 cm), Two seater sofa: Length (133 cm), Width (92 cm), Height (88 cm)
Seat filling: Foam with spring','couch',32998,49999,1);

INSERT INTO product VALUES (2,676743545,'Amazon Brand - Solimo Alen 5 Seater Fabric RHS L Shape Sofa Set (Grey)','Sectional','Solimo','Modern','Living Room',null,'Grey',5,'L-Shape',null,'Space saving','L Shaped Five-seater sofa with lounger; Sofa set - Length (50 inch), width (30 inch), height (31 inch) and Lounger - Length (72 inch), width (30 inch), height (31 inch)
Made with high quality fabric in grey color
Over 30 tests conducted to ensure quality
Fabric does not lose color while rubbing
Passed durability testing with 100 kg on each seat and backrest for 25,000 cycles
Meets Indian Standards IS 12674/ IS 5416 for performance and stringent European Safety Requirement Standard EN 12520
Warranty on manufacturing defects: 3 years','couch',29799,39999,1);

INSERT INTO product VALUES (3,676743545,'Amazon Brand - Solimo Alen 5 Seater Fabric RHS L Shape Sofa Set (blue)','Sectional','Solimo','Modern','Living Room',null,'blue',5,'L-Shape',null,'Space saving','L Shaped Five-seater sofa with lounger made from high-quality fabric in grey color
Product Dimensions: Sofa set - Length (50 inch), width (30 inch), height (31 inch) and Lounger - Length (72 inch), width (30 inch), height (31 inch)
Over 30 tests conducted to ensure quality
Fabric does not lose color while rubbing
Passed durability testing with 100 kg on each seat and backrest for 25,000 cycles
Meets Indian Standards IS 12674/ IS 5416 for performance and stringent European Safety Requirement Standard EN 12520
Warranty on manufacturing defects: 3 years
Lightweight for easy shifting
Good ground clearance for easy cleaning below the sofa
Free from toxins and harmful chemicals like formaldehyde and AZO Dye. Please note: Sofa is delivered with the legs in a detached condition. The legs are packed in a separate package and will be installed during assembly','couch',29799,44999,1);

INSERT INTO product VALUES(4,44598942,'Adorn India Chandler L Shape 5 Seater Sofa Set Stripes (Right Hand Side) (Beige)','Sectional','Adorn India','Modern','Living Room',null,'Beige 1','5','L-Shape',null,null,'Product dimension in cm Package 1 = Length (213.36) sofa Breadth (76.20) Lounger Breadth (160.02) height (66.04) sitting height (41.91)
Primary Material: Wood, secondary material :Foam Upholstery Material: Fabric : color : Beige
Warranty : 1 year warranty for frame and foam ( We provide service warranty only for major materials If Wood Gets Broken, Or Foam Gets Sink & never come back till one hour in its original shape, only in this two conditions you can claim warranty, And foam gets soft that is in its nature after regular use & There Is No Warranty For Fabric, Stitches, zipper Or Legs Get Bend Or Damage Or foam gets soft.)
No assembly required the product is delivered in a preassembled state.(only legs to be fix by the customer)
Please expect an unevenness of up to 1cm in the product due to differences in surfaces and floor levels.The color of the product may vary slightly compared to the picture displayed on your screen.this is due to lighting,pixel quality and color settings.Please check the product dimensions to ensure the product will fit in the desired location. Also, check if the product will fit through the entrance(s) and door(s) of the premises.','couch',19999,29999,1);

INSERT INTO product VALUES (5,535421335,'SMF Industry Wooden 4 Seater Sofa Set for Living Room | 2+1+1 Seater Sofa for Office & Lounge | Four Seater Sofa Sets for Home | Sheesham Wood, Rustic Teak','solid','SMF Industry','Modern',null,null,'Rustic Teak Brown',4,null,'Sheesham Wood','Portable, Termite Free','Product Dimensions(In Inch): Single Seater: Length 29 X Width 27 X Height 30 | 2 Seater: Length 52.4 X Width 27 X Height 30
All Seats base & backrest cushions are included and not small cushions, All Seat covers are removable & washable. And the cushions color is Cream and instruction required to assemble the products comes within the packet only.
Primary Material: Sheesham Wood | Secondary Material: MDF | Product Name: Wooden Four Seater Sofa For Living Room & Office.
Assembly Or Installation Is Based On Diy (Do It Yourself) Basis.
We Provide The Best Quality Products. Every Product Goes Through A Tough Quality Check To Ensure That We Can Serve Our Best Way. Only Made In India Products
Cushions Density - 32 , Back Rest Cushion - 3.5 Inches , Seating Cushion - 4.5 Inches , Cushions Cover with Zip Facility , Easy to Remove & Wash
In Absence Of A Service Lift, Our Delivery Partner Shall Only Make A Delivery To The Ground Floor Of Your Apartment. Extra Charges Applicable Per Floor On Delivery To The Customer?S Floor (On Request) In Such Cases.
If A Customer Wants To Claim Warranty , Share Photos And Videos Of Defect Parts , If We Find Manufacturing Issues , Defect Parts Will Be Return & Replaced, But Customers Have To Pack The Product Back In The Original Condition For Arranging The Successful Return Pickup For Replacement.
10 Days Replacement Only: This Item Is Eligible For Free Replacement, Within 10 Days Of Delivery, In An Unlikely Event Of Damaged, Defective Or Different/Wrong Item Delivered To You. Please Keep The Item In Its Original Condition, Original Packaging, With User Manual, Warranty Cards, And Original Accessories In Manufacturer Packaging For A Successful Return Pick-Up.
Buy With Confidence: Designed And Manufactured By SMF Industry. The Trusted Source For Stylish Furniture. For Every Taste And Budget.','couch',24501,29999,1);

INSERT INTO product VALUES(6,64544777,'Prima 5008 Center Trolley Coffee Table/Tea Table/Teapoy for Home, Office & Outdoor (Weather Brown)',null,'Prima','Contemporary',null,null,'Weather Brown',null,null,'Plastic',null,'Made of 100% Virgin Plastic: Provides the ultimate strength and durability to the product.
Safe and Non-Toxic: Only the highest quality of plastic is used in our products with rigorous safety tests.
High Load Bearing Capacity: Rigorously tested for safety and high-load bearing capacity.
Made in India
Quick and Easy Assembly: Follow a few simple steps provided with the package to assemble and enjoy your product!
Easy to Clean: Simply wipe down with a cloth and it will shine as good as new.
Low Maintenance: Assured elimination of any hassles or stress with Prima products!','teapoy',1199,1500,1);
select * from product;
drop table product;

delete from product where srno = 7;