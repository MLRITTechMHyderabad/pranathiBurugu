create database used_cars_dataset;
use used_cars_dataset;

drop table if exists used_cars;
CREATE TABLE used_cars(Make VARCHAR(255), Model VARCHAR(255), Year INT, Price INT, Mileage INT, BodyType VARCHAR(255),
	Cylinders NUMERIC(5,2), Transmission VARCHAR(255), FuelType VARCHAR(255), Color VARCHAR(255), Location VARCHAR(255), Description VARCHAR(255));
    
desc used_cars;