# import necessary libraries
import csv
import json
from tabulate import tabulate
import os
import re
import datetime
from datetime import datetime
import psycopg2

# create class with instances

class Permission():
    def __init__(self):
        
        self.name = ""
        self.description = ""

    def ask(self,name,description): # ask user input
        self.name = name
        self.description = description

# create check constraints for name input
    def name_constraint(self):

        while True:
            self.name = input("Enter permission name: ")

            if self.name == "":
                print("You can't leave empty")
                continue
            if not self.name.replace(" ","").isalnum():
                print("Invalid role")
                continue
            if self.name.isspace() == True:
                print("Invalid description")
                continue
            else:
                break

# create check constraints for role description
    def description_constraint(self):

        while True:

            self.description = input("Enter role description: ")

            if self.description == "":
                print("Can't be empty")
                continue
            if not self.description.replace(" ","").isalnum():
                print("Invalid text...Try again!")
                continue
            if self.description.isspace() == True:
                print("Invalid description")
                continue
            else:
                break



if __name__ == "__main__":

# convert class object in dictionary
    obj = Permission()

    obj.name_constraint()
    obj.description_constraint()

    obj1 = [obj.__dict__]
    print(obj1)

# create function for save class object dictionary

    def save_data():

        while True:

            print("                   1: Save Data")
            print("                   2: Create Another Permission")
            print("                   3: Update Permission")
            print("                   4: Delete Permission")
            print("                   5: List of Permission")
            print("                   6: Exit")

            user_input = input("What would youlike to do?: ")

            if user_input == "1":
                # create connection to databse

                try:
                    conn = psycopg2.connect("postgresql://postgres:computer@localhost/ecommerce")
                    
                except psycopg2.Error as e:
                
                    print(e)
                # get crusor
                try:
                    cur = conn.cursor()

                except psycopg2.Error as e:

                    print("Error: Couldn't get the crusor for the database")
                    print(e)
                conn.set_session(autocommit=True)

                
                # create table
                try:
                    cur.execute("CREATE TABLE IF NOT EXISTS user_schema.permissions(permission_id SERIAL PRIMARY KEY, \
                                p_name VARCHAR(50), p_description VARCHAR(70));")
                except psycopg2.Error as e:
                    print("Error: Issue with creating table")
                    print(e)

                # retrive data from table to check duplicate value
                cur.execute("SELECT p_name FROM user_schema.permissions")
                check_existing_data = cur.fetchall()

                # retrive data and store in a list
                column_existing_data = []
                for row in check_existing_data:
                    for v in row:
                        column_existing_data.append(v)

                # object class dictionary data 
                values = [v for k, v in obj1[0].items()]
                column_p_name = values[0] # first column data

                # compare and proceed with conditions
                if len(column_existing_data) == 0:
                    sql = "INSERT INTO  user_schema.permissions(p_name,p_description) VALUES ({})".format(','.join(['%s'] * len(values)))
                    cur.execute(sql, values)
                else:
                    for row in column_existing_data:
                        if row == column_p_name:
                            print("Permission name already  exists")
                            break
                        else:
                            sql = "INSERT INTO  user_schema.permissions(p_name,p_description) VALUES ({})".format(','.join(['%s'] * len(values)))
                            cur.execute(sql, values)
                       


                
            elif user_input == "2":

                obj.name_constraint()
                obj.description_constraint()

            else:
                exit()



    save_data()



            



    




