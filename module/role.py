import os
import psycopg2
import datetime
import csv

class Role():
    def __init__(self) -> None:
        
        self.name = ""

    def ask(self, name):
        self.name = name


    def rolename_constraint(self):
        while True:
            self.name = input("Enter role name: ")

            if self.name == "":
                print("Can't be empty")
                continue
            if not self.name.replace(" ","").isalnum():
                print("Invalid role name")
                continue
            if len(self.name) >= 50:
                print("Name should not more then 50 char")
                continue
            else:
                break

if __name__ == "__main__":


    obj = Role()
    obj.rolename_constraint()

    obj1 = [obj.__dict__]
    print(obj1)

    def save_data():
        while True:

            print("                   1: Save Data")
            print("                   2: Create Another User")
            print("                   3: Update User")
            print("                   4: Delete User")
            print("                   5: List of Users")
            print("                   6: Exit")

            user_input = input("What would ypu like to do: ")

            csv_data = "data/role.csv"
            dict_column = ["name"]
            data = obj1

            if user_input == "1":

               
                path = "data/role.csv"

                if os.path.exists(path):
                    with open(csv_data, 'a+') as add_data:
                        writer = csv.DictWriter(add_data,fieldnames=dict_column)

                        for record in data:
                            writer.writerow(record)
                else:
                    try:

                        with open(csv_data,'w') as write_data:
                            writer = csv.DictWriter(write_data,fieldnames=dict_column)
                            writer.writeheader

                            for record1 in data:
                                writer.writerow(record1)
                    except IOError:
                        print("I/O Error")


                
                conn= psycopg2.connect("postgresql://postgres:computer@localhost/ecommerce")
                

                try:
                    cur = conn.cursor()

                except psycopg2.Error as e:
                    print("Could not get crusor to the database")
                    print(e)

                conn.set_session(autocommit=True)


                try:
                    cur.execute("CREATE TABLE IF NOT EXISTS user_schema.user_role(role_id SERIAL PRIMARY KEY,role_name VARCHAR(50));")
                except psycopg2.Error as e:
                    print("Issue with creating table")
                    print(e)

                cur.execute("SELECT role_name FROM user_schema.user_role")
                existing_role = cur.fetchall()
               

                existing_role_data = []

                for row in existing_role:
                    for v in row:
                        existing_role_data.append(v)


                values = [v for k, v in obj1[0].items()]
                object_name_column = values[0] 

                if len(existing_role_data) == 0:
                    sql = "INSERT INTO  user_schema.user_role(role_name) VALUES ({})".format(','.join(['%s'] * len(values)))
                    cur.execute(sql, values)

                
                else:
                    for row in existing_role_data:
                        if row == object_name_column:
                            print("Role already Exisit")
                            break
                        else:
                            sql = "INSERT INTO  user_schema.user_role(role_name) VALUES ({})".format(','.join(['%s'] * len(values)))
                            cur.execute(sql, values)
                        

            elif user_input == "2":
                obj.rolename_constraint()

            else:
                exit()

                



    save_data()