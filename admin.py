import datetime as dt

import data
from data import food_details_list


def add_food_item():
    name = input("Name: ")
    quantity = input("Quantity: ")
    price = input("Price: ")
    discount = input("Discount(%): ")
    stock = input("Stock: ")
    admin_user = Admin(name,quantity,price,discount,stock)


class Admin:

    def __init__(self,name,quantity,price,discount, stock):
        self.food_id = dt.datetime.now().strftime("%m%d%Y%H%M%S")
        food_details_list.append({'food_id': self.food_id, 'name': name, 'quantity': quantity, 'price': price, 'discount': discount,
                          'stock': stock,'active':'True'})
        print("item added, Food Id :", self.food_id)

    def edit_food_item(food_id):
        edit_item = None
        for item in food_details_list:
            if item['food_id'] == food_id:
                edit_item = item
                break
        if edit_item is None:
            print(food_id, "not found")
        else:
            print(edit_item)
            name = input("Updated Name: ")
            quantity = input("Updated Quantity: ")
            price = input("Updated Price: ")
            discount = input("Updated Discount(%): ")
            stock = input("Updated Stock: ")
            food_details_list.remove(edit_item)
            food_details_list.append({'food_id': food_id, 'name': name, 'quantity': quantity, 'price': price, 'discount': discount,
                 'stock': stock,'active':'True'})
            print('item updated successfully')

    def view_all_foos_items():
        for item in food_details_list:
            if item['active'] == 'True':
                for key in item:
                  print(key,":",item[key])
        print('.................................')
    def delete_food_item(food_id):
        delete_item = None
        for item in food_details_list:
            if item['food_id'] == food_id:
                delete_item = item
                break
        if delete_item is None:
            print(food_id, "not found")
        else:
            food_details_list.remove(delete_item)
            delete_item['active'] = 'False'
            food_details_list.append(delete_item)
            print(delete_item['name'], "successfully deleted")


def admin_function():
    while True:
        print('1) Add new food item ')
        print('2) Edit food item ')
        print('3) View All food items ')
        print('4) Remove food item ')
        print("enter 0 to logout ")
        choose = int(input())
        if choose == 0:
            return
        elif choose == 1:
            add_food_item()
        elif choose == 2:
            Admin.edit_food_item(input("enter food id: "))
        elif choose == 3:
            Admin.view_all_foos_items()
        elif choose == 4:
            Admin.delete_food_item(input("enter food id: "))
        data.update_files()

