import os
import psycopg2

def get_clients(limit):
    query = "SELECT * FROM clients LIMIT %s;"
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (limit,))
            clients = cursor.fetchall()
    return clients

def get_client_by_id(client_id):
    query = "SELECT * FROM clients WHERE client_id = %s;"
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (client_id,))
            client = cursor.fetchone()
    return client

def make_client(client_name, client_phone):
    query = ("INSERT INTO clients (client_name, client_phone)"
             "VALUES (%s, %s);")
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (client_name, client_phone,))

def remove_client_by_id(client_id):
    query = "DELETE FROM clients WHERE client_id = %s;"
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (client_id,))

def establish_connection():
    return psycopg2.connect(
        host=os.getenv("DATABASE_HOST"),
        database=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD")
    )
