CREATE TABLE "admin" (
	"id" INT NOT NULL,
	"login" VARCHAR2(255) UNIQUE NOT NULL,
	"password" VARCHAR2(255) NOT NULL,
	constraint ADMIN_PK PRIMARY KEY ("id"));


CREATE TABLE "customer" (
	"id" INT NOT NULL,
	"email" VARCHAR2(255) UNIQUE NOT NULL check
     ( "email" LIKE '%@%.%'),
	"password" VARCHAR2(255) NOT NULL,
	constraint CUSTOMER_PK PRIMARY KEY ("id"));


CREATE TABLE "product" (
	"id" INT NOT NULL,
	"name" VARCHAR2(50) NOT NULL,
	"count" INT NOT NULL,
	"price" FLOAT NOT NULL,
	"photo" VARCHAR2(255),
	"type" INT NOT NULL,
	constraint PRODUCT_PK PRIMARY KEY ("id"));


CREATE TABLE "cart" (
	"id" INT NOT NULL,
	"purchase_id" INT NOT NULL,
	"customer_id" INT NOT NULL,
	constraint CART_PK PRIMARY KEY ("id"));


CREATE TABLE "cart_content" (
	"id" INT NOT NULL,
	"count" INT NOT NULL,
	"product_id" INT NOT NULL,
	"cart_id" INT NOT NULL,
	constraint CART_CONTENT_PK PRIMARY KEY ("id"));


CREATE TABLE "purchase" (
	"id" INT NOT NULL,
	"date" TIMESTAMP NOT NULL,
	"total_price" FLOAT NOT NULL,
	constraint PURCHASE_PK PRIMARY KEY ("id"));



CREATE TABLE "customer_phone" (
	"id" INT NOT NULL,
	"phone" NUMBER(10, 0) UNIQUE NOT NULL,
	"customer_id" INT NOT NULL,
	constraint CUSTOMER_PHONE_PK PRIMARY KEY ("id"));


CREATE TABLE "customer_address" (
	"id" INT NOT NULL,
	"address" VARCHAR2(255) NOT NULL,
	"customer_id" INT NOT NULL,
	constraint CUSTOMER_ADDRESS_PK PRIMARY KEY ("id"));




ALTER TABLE "cart" ADD CONSTRAINT "cart_fk0" FOREIGN KEY ("purchase_id") REFERENCES "purchase"("id");
ALTER TABLE "cart" ADD CONSTRAINT "cart_fk1" FOREIGN KEY ("customer_id") REFERENCES "customer"("id");

ALTER TABLE "cart_content" ADD CONSTRAINT "cart_content_fk0" FOREIGN KEY ("product_id") REFERENCES "product"("id");
ALTER TABLE "cart_content" ADD CONSTRAINT "cart_content_fk1" FOREIGN KEY ("cart_id") REFERENCES "cart"("id");


ALTER TABLE "customer_phone" ADD CONSTRAINT "customer_phone_fk0" FOREIGN KEY ("customer_id") REFERENCES "customer"("id");

ALTER TABLE "customer_address" ADD CONSTRAINT "customer_address_fk0" FOREIGN KEY ("customer_id") REFERENCES "customer"("id");