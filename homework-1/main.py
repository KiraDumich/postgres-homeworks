"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

# with open('north_data/customers_data.csv', newline='', encoding='utf-8') as csvfile:
#     file_reader = csv.reader(csvfile, delimiter=",")
#     data = []
#     for row in file_reader:
#         data.append(tuple(row))
#     with psycopg2.connect(host="localhost", database="north", user='postgres', password="KiDu2005") as conn:
#         with conn.cursor() as cur:
#             cur.executemany("INSERT INTO customers VALUES(%s,%s,%s)", data)
#             cur.execute("SELECT * FROM customers ")
#             conn.commit()

with open('north_data/employees_data.csv', newline='', encoding='utf-8') as csvfile:
    file_reader = csv.reader(csvfile, delimiter=",")
    data = []
    for row in file_reader:
        data.append(tuple(row))
    with psycopg2.connect(host="localhost", database="north", user="postgres", password="KiDu2005") as conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO employees VALUES(%s,%s,%s,%s,%s,%s)", data)
            cur.execute("SELECT * FROM employees")
            conn.commit()

with open('north_data/orders_data.csv', newline='', encoding='utf-8') as csvfile:
    file_reader = csv.reader(csvfile, delimiter=",")
    data = []
    for row in file_reader:
        data.append(tuple(row))
    with psycopg2.connect(host="localhost", database="north", user="postgres", password="KiDu2005") as conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO orders VALUES(%s,%s,%s,%s,%s)", data)
            cur.execute("SELECT * FROM orders")
            conn.commit()


