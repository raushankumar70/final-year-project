import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="1234",database="deepface")
cur=db.cursor()
cur.execute("create table dataa(user varchar(20),emial varchar(40),pwd(15)")
print("successfully")
