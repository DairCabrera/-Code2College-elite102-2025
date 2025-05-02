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


def main_menu():
    test_menu = int(input("what would you like to do?(1 withdraw, 2 deposite, 3 modify acount, 4 delete acount."))
    if test_menu == 1:
        print("choice")
    elif test_menu == 2:
        print("choice")
    elif test_menu == 3:
        print("choice")
    elif test_menu == 4:
        print("choice")
    else:
        print("invalid")
        main_menu()


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
            main_menu()
            return
        else:
            print("Incorrect PIN.")
            return  # Exit the function after incorrect PIN
    else:
        print("Wrong name entered.")
        signin()

signin()

def withdraw