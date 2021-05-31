import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="75679Gm@",database="gaurav")
mycursor = mydb.cursor()
mycursor.execute("select * from student")
result = mycursor.fetchall()
for i in result:
    print(i)