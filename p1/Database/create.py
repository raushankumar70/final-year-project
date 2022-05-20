import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="1234")
cur=db.cursor()
cur.execute("create database deepface")
print("successfully")
