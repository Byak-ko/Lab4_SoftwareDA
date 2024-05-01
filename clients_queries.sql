CREATE TABLE IF NOT EXISTS clients (
	client_id SERIAL PRIMARY KEY,
	client_name VARCHAR(100) NOT NULL,
	client_phone VARCHAR(15) NOT NULL
);

INSERT INTO clients (
	client_name,
	client_phone
)
VALUES (
	'Tonny Frederiksen',
	'123456789'
);

INSERT INTO clients (
	client_name,
	client_phone
)
VALUES (
	'John Brown',
	'987654321'
);

INSERT INTO clients (
	client_name,
	client_phone
)
VALUES (
	'Tom Biden',
	'555444333'
);
