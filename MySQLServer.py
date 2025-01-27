import mysql.connector
from mysql.connector import Error


try:
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
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rhs@11341")
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")  
        print("Database 'alx_book_store' created successfully!")
        mydb.close()
        mycursor.close()
except mysql.connector.Error as e:
    print(f'An error occurred {e}')
    



