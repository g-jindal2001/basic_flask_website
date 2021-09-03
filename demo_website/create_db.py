import mysql.connector
import python_secrets

mydb = mysql.connector.connect(
    host = python_secrets.dbhost,
    user = python_secrets.dbuser,
    passwd = python_secrets.dbpass
)

my_cursor = mydb.cursor()

my_cursor.execute("create database demo_db")
my_cursor.execute("show databases")

for db in my_cursor:
    print(db)