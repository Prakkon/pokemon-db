import psycopg2
# CREATES A CURSOR OBJECT TO EXECUTE SQL QUERIES
# Inserting values --->
#cursor.execute('''
#               insert into pokemon (name,type,id) values ('Pikachu','Electric',1);
#               insert into pokemon (name,type,id) values ('Charmander','Fire',2);
#               insert into pokemon (name,type,id) values ('Squirtle','Water',3);
#               ''')

# Extracting values --->
def extract():

    conn = psycopg2.connect(
            dbname = 'postgres',
            user = 'postgres',
            password = "prak",
            host = 'localhost',
            port = '5432'
        )
    cursor = conn.cursor()
    cursor.execute('''select * from pokemon;''')
    rows = cursor.fetchall() # FETCHES ALL (REMAINING) ROWS OF A
    for row in rows:
        print(row)  # PRINTS THE SECOND COLUMN OF EACH ROW

    conn.commit()
    conn.close()

    return 0

    

#one = cursor.fetchone() # FETCHES THE NEXT ROW OF A QUERY RESULT SET
#print(one)
#rows = cursor.fetchall() # FETCHES ALL (REMAINING) ROWS OF A QUERY RESULT SET
#for row in rows:
#    print(row[0])  # PRINTS THE SECOND COLUMN OF EACH ROW

# user input values --->
def insertvalues():
    conn = psycopg2.connect(
        dbname = 'postgres',
        user = 'postgres',
        password = "prak",
        host = 'localhost',
        port = '5432'
    )
    cursor = conn.cursor()
    name = input("Enter your pokemon's name: ")
    type = input("Enter your pokemon's type: ")
    id = input("Enter your pokemon's id: ")

    query = '''insert into pokemon (name,type,id) values (%s,%s,%s);'''

    cursor.execute(query, (name, type, id))

    conn.commit()
    conn.close()

    return 0

 # EXECUTES THE SQL COMMAND WITH THE PROVIDED PARAMETERS

def menu():

    print("Welcome to the Pokemon Database. If you want to insert values, press 1. If you want to extract the data, press 2. To exit, press 3.")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        insertvalues()
        menu()
    elif choice == 2:
        extract()
        menu()
    elif choice == 3:
        exit()

    else:
        print("Invalid choice. Please try again.")
        menu()

menu()

print("Data extracted from table successfully")

