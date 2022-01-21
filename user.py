import data
import hashlib
import datetime as dt

user_id = None


def validateuser(username, password):
    for user in data.users:
        if user["username"] == username and user["password"] == password:
            global user_id
            user_id = user["user_id"]
            return True
    return False


def createuser():
    username = input("Full Name: ")
    phonenumber = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    password = input("Password: ")
    repassword = input("Re-Enter Password: ")
    while repassword != password:
        print("Password Doesnt Match")
        password = input("Password: ")
        repassword = input("Re-Enter Password: ")

    user = User(username,phonenumber,email,address,password)



def update_stock(food_ids):
    for item in food_ids:
        for food in data.food_details_list:
            if food["food_id"] == item:
                food["stock"] = int(food["stock"]) - 1


def validate_stock(order_list,order_dic):
    selected_orders = {}
    for i in order_list:
        for item in data.food_details_list:
            if item['food_id'] == order_dic[i]:
                if item['food_id'] in selected_orders:
                    selected_orders[item['food_id']] += 1
                else:
                    selected_orders[item['food_id']] = 1
    for food_id in selected_orders:
        for item in data.food_details_list:
            if item['food_id'] == food_id:
                if selected_orders[food_id] > int(item['stock']):
                    print('only',item['stock'],item['name'],'are available in stock')
                    print('you ordered',selected_orders[food_id])
                    print('please order again with value lesser than stock')
                    return False
    return True

class User:

    def __init__(self,username,phonenumber,email,address,password,user_id = None,update = False):
        if update:
            self.user_id = user_id
        else:
            self.user_id = dt.datetime.now().strftime("%m%d%Y%H%M%S")
        res = hashlib.sha256(password.encode())
        password = res.hexdigest()

        data.users.append({'user_id': self.user_id, 'username': username, 'phonenumber': phonenumber, 'email': email, 'address': address,
             'password': password})
        if update:
            print('updated successful')
        else:
            print("Account Created SuccessFully")
            print('please be noted that username for login is your full Name')


    def place_order():
        n = 1
        order_dic = {}
        selected_orders = []
        for item in data.food_details_list:
            if item['active'] == 'True' and int(item['stock']) > 0:
                print('%s)%s (%s) [INR %s]' % (n, item["name"], item["quantity"], item["price"]))
                order_dic[n] = item['food_id']
                n += 1
        if n == 1:
            print("No item is available to buy")
            return
        print('enter 0 to cancel')
        order = input("enter comma seperated order numbers, if multiple same orders then repeat order numbers: ")
        if order =='0':
            return
        order_list = list(map(int, order.split(',')))
        if validate_stock(order_list,order_dic) == False:
            return
        print("selected orders are :- ")
        totalamount = 0
        n = 1
        for i in order_list:
            for item in data.food_details_list:
                if item['food_id'] == order_dic[i]:
                    print('%s)%s (%s) [%s]' % (n, item["name"], item["quantity"], item["price"]))
                    n += 1
                    selected_orders.append(item['food_id'])
                    totalamount += int(item["price"]) - int(item["price"]) * float(item['discount']) / 100
                    break
        print('Total Amount after discount:', totalamount)
        order_confirm = int(input("enter 1 to confirm order, 0 to cancel: "))
        if order_confirm == 1:
            update_stock(selected_orders)
            data.orders.append({'user_id': user_id, 'orders': selected_orders, 'datetime': str(dt.datetime.now())})
            print("order placed")

    def user_order_history(user_id):
        no_orders_placed = True
        for val in data.orders:
            ordered_time = None
            order_id_count = {}
            if val['user_id'] == user_id:
                ordered_time = val['datetime']

                for item in val['orders']:
                    if item in order_id_count:
                        order_id_count[item] += 1
                    else:
                        order_id_count[item] = 1
                        no_orders_placed = False

            i = 1
            if ordered_time == None:
                continue
            print('ordered on:', ordered_time)
            for order in order_id_count:
                for item in data.food_details_list:
                    if item['food_id'] == order:
                        sno = str(i) + ')'
                        print(sno, item['name'], 'X', order_id_count[order])
                        i += 1

        if no_orders_placed:
            print('no orders placed yet')
        print("\n\n")


def update_user(user_id):
    print('updating user')
    username = input("Full Name: ")
    phonenumber = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    password = input("Password: ")
    repassword = input("Re-Enter Password: ")
    while repassword != password:
        print("Password Doesnt Match")
        password = input("Password: ")
        repassword = input("Re-Enter Password: ")
    tempuser = None
    for user in data.users:
        if user['user_id'] == user_id:
            tempuser = user
            break
    data.users.remove(tempuser)
    user = User(username, phonenumber, email, address, password, user_id=user_id,update=True)
    print("profile updated")

def user_function():
    while True:
        data.update_files()
        print('1) Place New Order')
        print('2) Order History')
        print('3) Update Profile')
        print("enter 0 to logout ")
        choose = int(input())
        if choose == 1:
            User.place_order()
        if choose == 2:
            User.user_order_history(user_id)
        if choose == 3:
            try:
                update_user(user_id)
            except Exception as ex:
                print(ex.agrs)
        if choose == 0:
            return
