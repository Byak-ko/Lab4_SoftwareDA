import os
import psycopg2

def get_inventory(limit):
    query = "SELECT * FROM inventory LIMIT %s;"
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (limit,))
            inventory_items = cursor.fetchall()
    return inventory_items

def get_inventory_item_by_id(item_id):
    query = "SELECT * FROM inventory WHERE item_id = %s;"
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (item_id,))
            inventory_item = cursor.fetchone()
    return inventory_item

def add_inventory_item(item_name, item_quantity, item_price):
    query = ("INSERT INTO inventory (item_name, item_quantity, item_price)"
             "VALUES (%s, %s, %s);")
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (item_name, item_quantity, item_price,))

def remove_inventory_item_by_id(item_id):
    query = "DELETE FROM inventory WHERE item_id = %s;"
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (item_id,))

def establish_connection():
    return psycopg2.connect(
        host=os.getenv("DATABASE_HOST"),
        database=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD")
    )
