import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="Bank",
    password="Davetali05"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM bank.`bank details`;"
mycursor.execute(sql)
myresult = mycursor.fetchall()
# print(myresult)

def signin():
    User = input("put your name here: ")
    sql_select_user = "SELECT * FROM bank.`bank details` WHERE User = %s"
    mycursor.execute(sql_select_user, (User,))
    user_data = mycursor.fetchone()

    if user_data:
        pin_input = input("insert pin:")
        sql_select_pin = "SELECT Pin FROM bank.`bank details` WHERE User = %s AND Pin = %s"
        mycursor.execute(sql_select_pin, (User, pin_input))
        pin_data = mycursor.fetchone()
        if pin_data:
            sql_bank_amount = "SELECT `User Balance` FROM bank.`bank details` WHERE `User` = %s AND `Pin` = %s"
            mycursor.execute(sql_bank_amount, (User, pin_input))
            myresult = mycursor.fetchall()
            current_balance = myresult[0][0]
            print(current_balance)
            return
        else:
            print("Incorrect PIN.")
            return  # Exit the function after incorrect PIN
    else:
        print("Wrong name entered.")
        signin()

signin()