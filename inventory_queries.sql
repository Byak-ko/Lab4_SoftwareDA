CREATE TABLE IF NOT EXISTS inventory (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    item_quantity INT NOT NULL,
    item_price DECIMAL(10, 2) NOT NULL
);

INSERT INTO inventory (
    item_name,
    item_quantity,
    item_price
)
VALUES (
    'Scissors',
    10,
    25.00
);

INSERT INTO inventory (
    item_name,
    item_quantity,
    item_price
)
VALUES (
    'Hairdryer',
    5,
    50.00
);

INSERT INTO inventory (
    item_name,
    item_quantity,
    item_price
)
VALUES (
    'Hairbrush',
    20,
    10.00
);