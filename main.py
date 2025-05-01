import mysql.connector

connection = mysql.connector.connect(host = "localhost", user = 'root', database = 'Bank', password = 'Davetali05')
connection.close()

("temp")