import os
import psycopg2

def get_services(limit):
    query = "SELECT * FROM services LIMIT %s;"
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (limit,))
            services = cursor.fetchall()
    return services

def get_service_by_id(service_id):
    query = "SELECT * FROM services WHERE service_id = %s;"
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (service_id,))
            service = cursor.fetchone()
    return service

def make_service(service_name, service_price):
    query = ("INSERT INTO services (service_name, service_price)"
             "VALUES (%s, %s);")
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (service_name, service_price,))

def remove_service_by_id(service_id):
    query = "DELETE FROM services WHERE service_id = %s;"
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (service_id,))

def establish_connection():
    return psycopg2.connect(
        host=os.getenv("DATABASE_HOST"),
        database=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD")
    )
