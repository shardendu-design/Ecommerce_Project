# import necessary libraries
import os
import psycopg2
import pandas
import re
import csv
import datetime
import json
import time
import getpass
import bcrypt
import string
from tabulate import tabulate

# Create Class object with instances
class User():
    def __init__(self):
        self.user_name = ""
        self.password = ""
        self.user_address = ""
        self.user_role = ""
        self.user_email = ""

    def ask(self,user_name,password,user_address,user_role,user_email):
        self.user_name = user_name
        self.password = password
        self.user_address = user_address
        self.user_role = user_role
        self.user_email = user_email

# add check constraints
    def user_name_constraint(self):
        while True:
            self.user_name = input("Enter User Name: ")

            if self.user_name == "":
                print("You can't go further without user name")
                continue

            if len(self.user_name)>=50:
                print("The length of user name can't be more the 50 char")
                continue
            if not self.user_name.replace(" ","").isalnum():
                print("Invalid User Name")
                continue
            else:
                break

    def pass_constraint(self):
        while True:
            self.password = getpass.getpass("Enter your password: ")
            if self.password == "":
                print("Password can't be empty..")
                continue
            if self.password.isspace():
                print("Invalid password")
                continue

            hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
            self.password = hashed_password
            return self.password
          

# add constraints

    def user_address_constraint(self):
        while True:
            self.user_address = input("Enter User Address: ")

            if len(self.user_address)>=50:
                print("The length of the address can't be more then 50 char")
                continue
            if not self.user_address.replace(" ","").isalnum():
                print("Invalid user address")
                continue
            else:
                break

# add constraints

    def user_role_constraint(self):
        while True:
            self.user_role = input("Enter user role: ")

            if self.user_role =="":
                print("You can't go further user role")
                continue


            if len(self.user_role)>=50:
                print("Number should not be more then 50 char")
                continue
            

            if not self.user_role.replace(""," ").isalnum():
                print("Invalid number! please try again..")
                continue
            else:
                break

    def user_email_constraint(self):
        while True:
            self.user_email = input("Enter user email: ")
            if self.user_email =="":
                print("You can't go further without user email")
                continue

            if len(self.user_email)>=40:
                print("Length should not be more then 40 char")
                continue
            regex_email = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

            if not re.search(regex_email, self.user_email):
                print("Invalid Email")
                continue
            else:
                break

if __name__ == "__main__":

    conn0 = psycopg2.connect("postgresql://postgres:computer@localhost/postgres")
    cur0 = conn0.cursor()

    cur0.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'ecommerce'")
    exists = cur0.fetchone()

    if exists:
        conn001 = psycopg2.connect("postgresql://postgres:computer@localhost/ecommerce")
        cur001 = conn001.cursor()
        cur001.execute("SELECT * FROM user_schema.user_data")
        rows = cur001.fetchall()

        headers = ['Id','Name','Password','Address','Role','Email']
        print("")
        print("                                                                        User List")
        print("")
        print(tabulate(rows,headers=headers,tablefmt="pretty"))
        
        # for row in rows:
        #     print("User List")
        #     print("-"*180)
            
        #     print(row,headers)
        #     print("-"*180)

    else:
        print("")
        headers = ["                                        THERE IS NO USER PLEASE CREATE ONE                                     "]
        ss = ""
        print(tabulate(ss,headers=headers,tablefmt="pretty"))
        print("")

    print("") 
    

    obj = User()
    obj.user_name_constraint()
    obj.pass_constraint()
    obj.user_address_constraint()
    obj.user_role_constraint()
    obj.user_email_constraint()

    obj1 = [obj.__dict__]
    print(obj1)


    def save_data():

        # save data as csv
        while True:

            print("                   1: Save Data")
            print("                   2: Create Another User")
            print("                   3: Update User")
            print("                   4: Delete User")
            print("                   5: List of Users")
            print("                   6: Exit")

            user_input = input("What would you like to do?")

            data = obj1
            csv_file = "data/user.csv"
            dict_column = ["user_name","password","user_address","user_role","user_email"]

            if user_input == "1":
                path = "data/user.csv"
                if os.path.exists(path):
                    with open(csv_file, "a+") as add_record:
                        writer = csv.DictWriter(add_record, fieldnames=dict_column)

                        for record in data:
                            writer.writerow(record)

                else:
                    try:
                        
                        with open(csv_file, "w") as write_file:
                            writer = csv.DictWriter(write_file, fieldnames=dict_column)
                            writer.writeheader

                            for record1 in data:
                                writer.writerow(record1)
                    except IOError:
                        print("I/O Error")


                conn1 = psycopg2.connect("postgresql://postgres:computer@localhost/postgres")
                conn1.autocommit=True

                cur1 = conn1.cursor()
                cur1.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'ecommerce'")
                exists = cur1.fetchone()

                if not exists:
                    cur1.execute("CREATE DATABASE ecommerce")

                conn1.set_session(autocommit=True)

                try:
                    conn = psycopg2.connect("postgresql://postgres:computer@localhost/ecommerce")
                except psycopg2.Error as e:
                    print("e")

                try:
                    cur = conn.cursor()
                except psycopg2.Error as e:
                    print("Error: Could not get the cruser to the databse")
                    print(e)

                conn.set_session(autocommit=True)

                try:
                    cur.execute("CREATE SCHEMA IF NOT EXISTS user_schema;")
                except psycopg2.Error as e:
                    print("Error: Issue creating schema")
                    print(e)

                try:
                    cur.execute("CREATE TABLE IF NOT EXISTS user_schema.user_data(user_id SERIAL PRIMARY KEY, \
                                user_name VARCHAR(50) NOT NULL, user_password VARCHAR NOT NULL, user_address VARCHAR(70), user_role VARCHAR(50), \
                                user_email VARCHAR(50));")
                except psycopg2.Error as e:
                    print("Error: Issue creating table")
                    print(e)


              
                
                values  = [v for k, v in obj1[0].items()]
                sql = "INSERT INTO  user_schema.user_data(user_name,user_password,user_address,user_role,user_email) VALUES ({})".format(','.join(['%s'] * len(values)))
                cur.execute(sql, values)

            

            elif user_input == "2":
                obj.user_name_constraint()
                obj.pass_constraint()
                obj.user_address_constraint()
                obj.user_role_constraint()
                obj.user_email_constraint()

           

            else:
                exit()

            

    save_data()





                