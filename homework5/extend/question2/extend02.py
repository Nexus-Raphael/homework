import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="nexus"
)

cursor = connection.cursor()

#sql = "delete from winefactory where name = 'VODKA'"
cursor.execute("update winefactory set id = id - 1 where id >2")
#cursor.execute(sql)
connection.commit()

cursor.close()
connection.close()
#我是先做完#的那两句才用14行的，所以图片不太一样