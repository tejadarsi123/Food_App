import os
import json
import datetime as dt

food_details_list = []
orders = []
users = []


def read_Files():
    try:
        with open('food_details_list.txt', 'r') as fptr:
            data = fptr.readlines()
            for line in data:
                food_details_list.append(json.loads(line.replace("'",'"')))


        with open('orders.txt', 'r') as fptr:
            data = fptr.readlines()
            for line in data:
                orders.append(json.loads(line.replace("'",'"')))

        with open('users.txt', 'r') as fptr:
            data = fptr.readlines()
            for line in data:
                users.append(json.loads(line.replace("'",'"')))
    except Exception as ex:
        error = ex

def update_files():
    try:
        with open('food_details_list.txt', 'w') as fptr:
            for line in food_details_list:
                fptr.writelines(str(line) +"\n")

        with open('orders.txt', 'w') as fptr:
            for line in orders:
                fptr.writelines(str(line) +"\n")

        with open('users.txt', 'w') as fptr:
            for line in users:
                fptr.writelines(str(line) + "\n")

    except Exception as ex:
        print(ex.args)

