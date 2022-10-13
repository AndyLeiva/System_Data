import sqlite3 as sql


# create_database
def create_database():
    connect_db = sql.connect(name_database)
    connect_db.commit()
    connect_db.close()

# create_database with 4 columns: id, name, lastname, password, age
def create_table():
    connect_db = sql.connect(name_database)
    cursor = connect_db.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            
            name text,
            lastname text,
            password text,
            age integer
            )"""
    )
    connect_db.commit()
    connect_db.close()

# insert data in table
def insert_Row(name,lastname, password,age,name_database):
    connect_db = sql.connect(name_database)
    cursor = connect_db.cursor()
                    #                           id,name,lastname, password, age
                    # with null the id can autoincrement
    instruction = f"INSERT into account VALUES(null,'{name}','{lastname}','{password}','{age}')"
    cursor.execute(instruction)
    print("Account created!")
    connect_db.commit()
    connect_db.close()

# Searchs the name of the Account 
def search(name):
    connect_db = sql.connect(name_database)
    cursor = connect_db.cursor()
    instruccion = f"SELECT * FROM account WHERE name = '{name}'"
    cursor.execute(instruccion)
    data = cursor.fetchall()
    connect_db.commit()
    connect_db.close()
    

    return data # Return a list with a tuple of data consulted



    

if __name__ == "__main__":
    global name_database
    name_database = "accounts.db"
    create_database()
    create_table()
    
    
            
    
     
        
       
   


    

    
    