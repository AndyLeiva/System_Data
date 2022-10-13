import database as db

class Login():

    def __init__(self, name, password):
        self.name = name
        self.password = password

# Method to search the account is requested with name. 
# Later with the data in memory, it is verificated the password
# If the name and password are correct the User can Login into the System Successfuly!
    def Search_Account(self):

        data_account = db.search(self.name)

        while data_account == []:
            print("No account found")
            
            self.name = input("Enter your name: ")
            data_account = db.search(self.name)


    # [0] is the position of the tuple of account and 
    # [3] is the position of the password    

        Password_Consulted = data_account[0][3]  

        if Password_Consulted != self.password:

            attemps = 2
            while attemps <= 2 and attemps >= 1:
                print("Incorrect Password")
                attemps = attemps-1

                Password_Input = input("What is your Password?: ")

                if  Password_Input == Password_Consulted:
                    print("Welcome to the system!")
                    break
        else:   

            print("Welcome to the system!") 




# Creating object Account and request of NAME AND password

name_input = input("What is your name?: ")
password_input = input("What is your password?: ")

Account = Login(name_input,password_input)
Account.Search_Account()


