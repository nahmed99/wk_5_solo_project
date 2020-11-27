DROP TABLE repairs;
DROP TABLE mechanics;
DROP TABLE cars;

CREATE TABLE mechanics (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    mot_qualified BOOLEAN
);

CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    registration_number VARCHAR(255),
    make VARCHAR(255),
    model VARCHAR(255),
    mot_renewal_date DATE 
);

CREATE TABLE repairs (
    id SERIAL PRIMARY KEY,
    mechanic_id INT REFERENCES mechanics(id) ON DELETE CASCADE,
    car_id INT REFERENCES cars(id) ON DELETE CASCADE,
    repair_date DATE
    details VARCHAR(255)
);