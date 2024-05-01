CREATE TABLE IF NOT EXISTS services (
    service_id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    service_price DECIMAL(10, 2) NOT NULL
);

INSERT INTO services (
    service_name,
    service_price
)
VALUES (
    'Haircut',
    20.00
);

INSERT INTO services (
    service_name,
    service_price
)
VALUES (
    'Hair dye',
    50.00
);

INSERT INTO services (
    service_name,
    service_price
)
VALUES (
    'Hairstyle',
    30.00
);	