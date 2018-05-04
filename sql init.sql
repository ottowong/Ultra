BEGIN;
--
-- Create model DeliveryAddress
--
CREATE TABLE "main_deliveryaddress" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "firstName" varchar(200) NOT NULL, "lastName" varchar(200) NOT NULL, "address1" varchar(200) NOT NULL, "address2" varchar(200) NOT NULL, "address3" varchar(200) NOT NULL, "stateCounty" varchar(200) NOT NULL, "city" varchar(200) NOT NULL, "country" varchar(200) NOT NULL, "postcode" varchar(200) NOT NULL);
--
-- Create model Order
--
CREATE TABLE "main_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "status" integer NOT NULL, "deliveryAddressId_id" integer NOT NULL REFERENCES "main_deliveryaddress" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model OrderItem
--
CREATE TABLE "main_orderitem" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" integer NOT NULL, "orderId_id" integer NOT NULL REFERENCES "main_order" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Product
--
CREATE TABLE "main_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "description" varchar(200) NOT NULL, "image" text NOT NULL, "price" decimal NOT NULL);
--
-- Create model Type
--
CREATE TABLE "main_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL);
--
-- Create model User
--
CREATE TABLE "main_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "firstName" varchar(200) NOT NULL, "lastName" varchar(200) NOT NULL, "email" varchar(200) NOT NULL, "password" varchar(200) NOT NULL, "address1" varchar(200) NOT NULL, "address2" varchar(200) NOT NULL, "address3" varchar(200) NOT NULL, "stateCounty" varchar(200) NOT NULL, "city" varchar(200) NOT NULL, "country" varchar(200) NOT NULL, "postcode" varchar(200) NOT NULL, "admin" bool NOT NULL);
--
-- Add field typeId to product
--
ALTER TABLE "main_product" RENAME TO "main_product__old";
CREATE TABLE "main_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "description" varchar(200) NOT NULL, "image" text NOT NULL, "price" decimal NOT NULL, "typeId_id" integer NOT NULL REFERENCES "main_type" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "main_product" ("description", "name", "image", "id", "typeId_id", "price") SELECT "description", "name", "image", "id", NULL, "price" FROM "main_product__old";
DROP TABLE "main_product__old";
CREATE INDEX "main_order_deliveryAddressId_id_06042d77" ON "main_order" ("deliveryAddressId_id");
CREATE INDEX "main_orderitem_orderId_id_4b6c88b4" ON "main_orderitem" ("orderId_id");
CREATE INDEX "main_product_typeId_id_2aad3aa2" ON "main_product" ("typeId_id");
--
-- Add field productId to orderitem
--
ALTER TABLE "main_orderitem" RENAME TO "main_orderitem__old";
CREATE TABLE "main_orderitem" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" integer NOT NULL, "orderId_id" integer NOT NULL REFERENCES "main_order" ("id") DEFERRABLE INITIALLY DEFERRED, "productId_id" integer NOT NULL REFERENCES "main_product" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "main_orderitem" ("quantity", "orderId_id", "productId_id", "id") SELECT "quantity", "orderId_id", NULL, "id" FROM "main_orderitem__old";
DROP TABLE "main_orderitem__old";
CREATE INDEX "main_orderitem_orderId_id_4b6c88b4" ON "main_orderitem" ("orderId_id");
CREATE INDEX "main_orderitem_productId_id_3164afb2" ON "main_orderitem" ("productId_id");
--
-- Add field userId to order
--
ALTER TABLE "main_order" RENAME TO "main_order__old";
CREATE TABLE "main_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "status" integer NOT NULL, "deliveryAddressId_id" integer NOT NULL REFERENCES "main_deliveryaddress" ("id") DEFERRABLE INITIALLY DEFERRED, "userId_id" integer NOT NULL REFERENCES "main_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "main_order" ("status", "deliveryAddressId_id", "userId_id", "id") SELECT "status", "deliveryAddressId_id", NULL, "id" FROM "main_order__old";
DROP TABLE "main_order__old";
CREATE INDEX "main_order_deliveryAddressId_id_06042d77" ON "main_order" ("deliveryAddressId_id");
CREATE INDEX "main_order_userId_id_f63418f0" ON "main_order" ("userId_id");
COMMIT;
