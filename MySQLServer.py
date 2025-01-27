import mysql.connector
from mysql.connector import Error


try:

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rhs@11341",
        database="alx_book_store"
    )

    print("Database 'alx_book_store' created successfully!")
    mydb.close()
except Error as e:
    print(f'Server connection failed, Error: {e}')

