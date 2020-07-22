import sqlite3 as lite


# functionality goes here

class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = lite.connect('products.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS product(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a DB !")
        

    # TODO: create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO product(name, description, price, is_private) VALUES (?,?,?,?)", data
                    )
                return True
        except Exception:
            return False

    # TODO: read data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM product")
                return cur.fetchall()
        except Exception:
            return False

    # TODO: delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM product WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False


# TODO: provide interface to user

def main():
    print("*"*40)
    print("\n:: PRODUCT MANAGEMENT :: \n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()

    print("#"*40)
    print("\n :: User Interface :: \n")
    print("#"*40)

    print('\nPress 1. Insert a new PRODUCT\n')
    print('Press 2. Show all PRODUCT\n')
    print('Press 3. Delete a PRODUCT (NEED ID OF COURSE)\n')
    print("#"*40)
    print("\n")

    choice = input("\n Enter a choice: ")

    if choice == "1":
        name = input("\n Enter PRODUCT name: ")
        description = input("\n Enter PRODUCT description: ")
        price = input("\n Enter PRODUCT price: ")
        private = input("\n Is this PRODUCT private (0/1): ")

        if db.insert_data([name, description, price, private]):
            print("PRODUCT was inserted successfully")
        else:
            print("OOPS SOMEthing is wrong")


    elif choice == "2":
        print("\n:: Course List ::")

        for index, item in enumerate(db.fetch_data()):
            print("\n Sl no : " + str(index + 1))
            print("PRODUCT ID : " + str(item[0]))
            print("PRODUCT Name : " + str(item[1]))
            print("PRODUCT description : " + str(item[2]))
            print("PRODUCT Price : " + str(item[3]))
            private = 'Yes' if item[4] else 'NO'
            print("Is Private : " + private)
            print("\n")

    elif choice == "3":
        record_id = input("Enter the PRODUCT ID: ")

        if db.delete_data(record_id):
            print("PRODUCT was deleted with a success")
        else:
            print("OOPS SOMETHING WENT WRONG")

    else:
        print("\n BAD CHOICE")      



if __name__ == '__main__':
    main()