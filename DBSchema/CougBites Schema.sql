CREATE TABLE Locations (
	location_id VARCHAR UNIQUE,
	location_name VARCHAR,
	address VARCHAR,
	location_pic BYTEA,
	opening_hours TIME ARRAY[7],
	closing_hours TIME ARRAY[7],
	PRIMARY KEY (location_id)
);

CREATE TABLE FoodItems (
	food_id VARCHAR UNIQUE,
	food_name VARCHAR,
	food_pic BYTEA,
	food_description VARCHAR,
	avg_rating INTEGER DEFAULT 0,
	PRIMARY KEY (food_id)
);

CREATE TABLE Users (
	user_id VARCHAR UNIQUE,
	username VARCHAR UNIQUE,
	email VARCHAR UNIQUE,
	password_hash VARCHAR UNIQUE,
	PRIMARY KEY (user_id)
);

CREATE TABLE Ratings (
	rating_value INTEGER CHECK (rating_value >= 0 AND rating_value <= 5),
	description VARCHAR,
	user_id VARCHAR,
	food_id VARCHAR,
	PRIMARY KEY (user_id, food_id),
	FOREIGN KEY (user_id) REFERENCES Users (user_id),
	FOREIGN KEY (food_id) REFERENCES FoodItems (food_id)
);

-- avail_days = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
-- avail_times = [breakfast, lunch, dinner]

CREATE TABLE FoodAvailability (
	availability BOOLEAN DEFAULT TRUE,
	avail_days BOOLEAN ARRAY[7],
	avail_times BOOLEAN ARRAY[3],
	food_id VARCHAR,
	location_id VARCHAR,
	PRIMARY KEY (food_id, location_id),
	FOREIGN KEY (food_id) REFERENCES FoodItems (food_id),
	FOREIGN KEY (location_id) REFERENCES Locations (location_id)
);

	
	
	