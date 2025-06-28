import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host = '192.168.126.218',
        username = 'root',
        password = 'COMPLI09060ment$'
    )

    if mydb.is_connected():
        print('Connection created successfully')

    mycursor = mydb.cursor()

    sql = ("CREATE DATABASE IF NOT EXISTS alx_book_store")
    mycursor.execute(sql)
    print("Database 'alx_book_store' created successfully!")

    mydb.commit()
except mysql.connector.Error as e:
    print(e)
finally:
    mycursor.close()
    mydb.close()

