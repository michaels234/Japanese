import mysql.connector


def database():
    mydb = mysql.connector.connect(
      host="localhost",
      user="mikey",
      password="pass"
    )

    print(mydb)

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE mydatabase")

    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
      print(x)