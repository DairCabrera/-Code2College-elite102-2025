import mysql.connector
import time
import os
import keyboard

connection = mysql.connector.connect(user = 'root', database = 'Bank', password = 'Davetali05')
connection.close()

print("Welcome to common banking app. What would you like to do?\noption1:<\noption1:\noption1:\noption1:")