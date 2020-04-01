-- Enum for the days
CREATE TABLE IF NOT EXISTS days
(
    id       SERIAL PRIMARY KEY,
    day_name VARCHAR
);

CREATE TABLE IF NOT EXISTS parking_lot
(
    id       SERIAL PRIMARY KEY,
    address  VARCHAR,
    capacity INT,
    CONSTRAINT address_ck UNIQUE (address)
);

CREATE TABLE IF NOT EXISTS hours
(
    id         SERIAL PRIMARY KEY,
    open_time  TIME,
    close_time TIME,
    day        INT REFERENCES days (id),
    CONSTRAINT hours_ck UNIQUE (open_time, close_time, day)
);

CREATE TABLE IF NOT EXISTS rates
(
    id          SERIAL PRIMARY KEY,
    hourly_rate DECIMAL,
    max_hourly  DECIMAL,
    flat_rate   DECIMAL,
    day         INT REFERENCES days (id),
    CONSTRAINT rates_ck UNIQUE (hourly_rate, max_hourly, flat_rate, day)
);

CREATE TABLE IF NOT EXISTS parking_lot_rates
(
    lot_id  INT REFERENCES parking_lot (id),
    rate_id INT REFERENCES rates (id),
    CONSTRAINT parking_lot_rates_pk PRIMARY KEY (lot_id, rate_id)
);

CREATE TABLE IF NOT EXISTS parking_lot_hours
(
    lot_id   INT REFERENCES parking_lot (id),
    hours_id INT REFERENCES hours (id),
    CONSTRAINT parking_lot_hours_pk PRIMARY KEY (lot_id, hours_id)
);

CREATE TABLE IF NOT EXISTS cars
(
    id             SERIAL PRIMARY KEY,
    entry_time     TIME,
    exit_time      TIME,
    parking_lot_id INT REFERENCES parking_lot (id)
);

CREATE TABLE IF NOT EXISTS users
(
    id         SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name  VARCHAR,
    address    VARCHAR,
    phone      VARCHAR,
    start_date DATE,
    role       INT,
    CONSTRAINT users_ck UNIQUE (first_name, last_name, phone),
    CONSTRAINT users_ck2 UNIQUE (first_name, last_name, phone, address)
);

CREATE TABLE IF NOT EXISTS keycards
(
    id               SERIAL PRIMARY KEY,
    access_type      INT,
    parking_lot_id   INT REFERENCES parking_lot (id),
    keycard_owner_id INT REFERENCES users (id),
    CONSTRAINT keycard_ck UNIQUE (parking_lot_id, keycard_owner_id)
);

CREATE TABLE IF NOT EXISTS parking_lot_keycards
(
    parking_lot_id INT REFERENCES parking_lot (id),
    keycard_id     INT REFERENCES keycards (id),
    CONSTRAINT parking_lot_keycards_pk PRIMARY KEY (parking_lot_id, keycard_id)
);


CREATE TABLE IF NOT EXISTS validation_types
(
    id              SERIAL PRIMARY KEY,
    validation_name VARCHAR
);

CREATE TABLE IF NOT EXISTS validations
(
    id              SERIAL PRIMARY KEY,
    validation_type INT REFERENCES validation_types (id),
    start_date      DATE,
    expiry_date     DATE,
    date_issued     TIME,
    parking_lot_id  INT REFERENCES parking_lot (id)
);

CREATE TABLE IF NOT EXISTS report
(
    id             SERIAL PRIMARY KEY,
    issued_on      TIMESTAMP,
    start_range    TIMESTAMP,
    end_range      TIMESTAMP,
    parking_lot_id INT REFERENCES parking_lot (id)
);


CREATE TABLE IF NOT EXISTS revenue_categories_list
(
    id                    SERIAL PRIMARY KEY,
    revenue_category_name VARCHAR
);


CREATE TABLE IF NOT EXISTS revenue_categories
(
    id               SERIAL PRIMARY KEY,
    revenue_category INT REFERENCES revenue_categories_list (id),
    quantity         INT
    revenue          DECIMAL
);


CREATE TABLE IF NOT EXISTS reports_revenue_categories
(
    revenue_category INT REFERENCES revenue_categories (id),
    report           INT REFERENCES report (id),
    CONSTRAINT parking_lot_keycards_pk PRIMARY KEY (report, revenue_category)
);