import database as db

class SignIn():

    def __init__(self, name, lastname, password, age):
        self.name = name
        self.lastname = lastname
        self.password = password
        self.age = age

    def insert_data(self):
        db.insert_Row(self.name, self.lastname, self.password, self.age)
        

name = input("What is your name?: ")
lastname = input("What is your lastname?: ")
age = int(input("What is your age?: "))

password = input("What is your password?: ")
confirm_password = input("Confirm your password: ")

while password!= confirm_password:
    print("Passwords do not match!")
    password = input("What is your password?: ")
    confirm_password = input("Confirm your password: ")
     



Create_Account = SignIn(name, lastname, password, age)
Create_Account.insert_data()