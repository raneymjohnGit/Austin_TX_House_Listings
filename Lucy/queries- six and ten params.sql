-- Creating tables for Austin_Housing_Listings

CREATE TABLE Seven_Parameters (
	city VARCHAR NOT NULL,
	zpid INT NOT NULL,
	zipcode INT NOT NULL,
	lotSizeSqFt VARCHAR NOT NULL,
	livingAreaSqFt INT NOT NULL,
	numOfBathrooms VARCHAR NOT NULL,
	numOfBedrooms INT NOT NULL,
	PRIMARY KEY (zpid)
);

CREATE TABLE Eleven_Parameters (
	city VARCHAR NOT NULL,
	zpid INT NOT NULL,
	zipcode INT NOT NULL,
	garageSpaces INT NOT NULL,
	hasAssociation VARCHAR NOT NULL,
	yearBuilt INT NOT NULL,
	lotSizeSqFt VARCHAR NOT NULL,
	livingAreaSqFt INT NOT NULL,
	numOfBathrooms VARCHAR NOT NULL,
	numOfBedrooms INT NOT NULL,
	numOfStories INT NOT NULL,
	PRIMARY KEY (zpid)
);