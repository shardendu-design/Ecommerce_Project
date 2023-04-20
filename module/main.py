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
    user_data()
    user_list()
    # company_list()
    # menu()

def login():
    while True:

        print("             Welcome to Online Shopping Mart")

        user_name = 'admin'
        user_input_name = input("Enter Login Name: ")
        user_password  = "admin"

        user_input_password = getpass.getpass("Enter Password: ")

        if user_input_name == user_name and user_input_password == user_password:
            print(" Welcome To Online Shopping Mart")
            break
        else:
            print("Invalid user and password..")

        print("                        1: Create New User")

        
        
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
    
    conn.set_session(autocommit=True)
    
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