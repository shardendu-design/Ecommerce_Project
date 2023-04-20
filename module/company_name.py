import os
import pandas
import csv
import json
import psycopg2
import datetime
import time
from datetime import datetime, timedelta
from datetime import date
import re



class Company():
    def __init__(self) -> None:
        self.company_name = ""
        self.start_date = ""
        self.end_date = ""
        self.address = ""
        self.phone = ""
        self.email = ""

    def ask(self,company_name,start_date,end_date,address,phone,email):
        self.company_name = company_name
        self.start_date = start_date
        self.end_date = end_date
        self.address = address
        self.phone = phone
        self.email = email

    def companu_name_constraint(self):
        while True:
            self.company_name = input("Enter company name: ")

            if self.company_name == "":
                print("You can't go further without company name..")
                continue

            if len(self.company_name)>=50:
                print("Compnay name should be less then 50 cahr")
                continue
            if not self.company_name.replace(""," ").isalnum:
                print("Invalid company name try again!..")
                continue
            else:
                break

    def start_date_constraint(self):
            
        self.start_date = date.today().strftime('%d-%m-%Y')
        print("Start Date: ", self.start_date)
        return self.start_date

    def end_date_constraint(self):

        end_date = date.today()
        future_date = end_date + timedelta(days=365)
        self.end_date = future_date.strftime('%d-%m-%Y')
        print("End Date: ", self.end_date)
        return self.end_date

       
    def address_constraint(self):
        while True:
            self.address = input("Enter company address: ")

            if self.address == "":
                print("You can't go further without address")
                continue
            if len(self.address)>=50:
                print("Address shoild be less then 50 char")
                continue
            if not self.address.replace(""," ").isalnum:
                print("Invalid address")
                continue
            else:
                break

    def phone_constraint(self):
        while True:
            self.phone = input("Enter phone number: ")

            if self.phone == "":
                print("You can't leave empty")
                continue
            if len(self.phone)>=50:
                print("The length should be less then 50 char")
                continue
            if not self.phone.replace(""," ").isalpha:
                print("Invalid phone number")
                continue

            regexp = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

            if not re.search(regexp, self.phone):
                print("Invalid phone number try again!..")
                continue

            else:
                break

    def email_constraint(self):
        while True:
            self.email = input("Enter company email: ")

            if self.email == "":
                print("You can't leave empty")
                continue

            if len(self.email)>=50:
                print("The length should be less then 50 char")
                continue

            if not self.email.replace(""," ").isalnum:
                print("Invalid email address..")
                continue

            regex_email = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
            if not re.search(regex_email, self.email):
                print("Invalid email address")
                continue
            else:
                break

           

if __name__ == "__main__":

    obj = Company()
    obj.companu_name_constraint()
    obj.start_date_constraint()
    obj.end_date_constraint()
    obj.address_constraint()
    obj.phone_constraint()
    obj.email_constraint()

    obj1 = [obj.__dict__]
    print(obj1)

    def save_data():
        while True:

            print("1: save data")
            print("2: Create another company")
            print("3: Exit")

            user_input = input("What would you like to do?: ")

            


            





