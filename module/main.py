import os
import datetime
import pandas as pd
import csv
import psycopg2
from tabulate import tabulate 
import getpass
import bcrypt
from prettytable import PrettyTable


def main():
    
    login()
    # user_data()
    # user_list()
    # company_list()
    # menu()

def login():
    while True:


        print("             Welcome to Online Shopping Mart")
        username = input("Enter Username: ")
        # password = input("Enter paswword: ")
        password = getpass.getpass("Enter Your Password : ")

        # create database connection
        conn = psycopg2.connect("postgresql://postgres:computer@localhost/ecommerce")

        try:

            # Create a cursor to execute SQL queries

            with conn.cursor() as cur:
               
                cur.execute("SELECT user_password,user_role FROM user_schema.user_data WHERE user_name =%s", (username,))    
                row = cur.fetchone()
                

                if row:
                    hashed_password = row[0]
                    role = row[1]
                    # print(hashed_password)
                    
                    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                        print("Login successful. User role: ", role)
                        return role
                else:
                    print("Invalid username and password")
                    continue
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to postgresql", error)

        finally:
            # Close the database connection
            if conn:
                conn.close()


                   
           
def user_data():

    conn = psycopg2.connect("postgresql://postgres:computer@localhost/ecommerce")
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM pg_namespace WHERE nspname = 'user_schema'")
    schema_exists = cur.fetchone()

    if schema_exists:
        cur.execute("SELECT * FROM user_schema.user_data")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    else:
        print("User Doesn't exists")
    
    # conn.set_session(autocommit=True)
    
    # with conn.cursor() as cur:
            
    #         cur.execute("SELECT 1 FROM pg_namespace WHERE nspname = 'user_schema'")
        
    #         schema_exists = cur.fetchone()
    #         if schema_exists:
    #             cur.execute("SELECT * FROM user_schema.user_data")
    #             rows =cur.fetchall()

    #             for row in rows:
    #                 print(row)

    #         else:
    #             print("user doesn't exisist please create it")
    #             print(user)
               
                
          
            #headers = ['Id','Name','Password','Address','Phone','Email']
            #print(tabulate(rows,headers,tablefmt='fancy_grid'))
    

    
    
            
def user_list():
    ss = os.system("python /Users/shardendujha/Ecommerce_Project/module/user.py")
    return ss

    

if __name__ == '__main__':
    main()