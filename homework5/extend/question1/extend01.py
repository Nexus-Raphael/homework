import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="nexus"
)

cursor = connection.cursor()

cursor.execute("create table winefactory (id int auto_increment primary key,name varchar(20),date varchar(10),choice varchar(5))")
#自增主键

sql = "insert into winefactory(name,date,choice) values (%s, %s, %s)"

val = [
    ("GIN", "1994", 'B'),
    ("VODKA", '1994', 'B'),
    ('SHERRY', '1994', 'R'),
    ('RYE_WHISKEY', '2001', 'R'),
    ('BINGA', '2023', 'B'),
]
cursor.executemany(sql, val)

connection.commit()
cursor.execute("select * from winefactory")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
connection.close()