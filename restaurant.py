# restaurant waiter helper program
menu = ["chicken soup", "roast duck with rice", "special fried rice", "pizza", "chips", "burger"]
print("In our menu, we have {}, {}, {}, {}, {} and {}".format(menu[0], menu[1], menu[2], menu[3], menu[4], menu[5]))
order_list = []
order_length = 1
promt = True
while promt:
    order = input("what would you like to order? ")
    order = order.lower()
    if order in menu:
        order_list.append(order)
        while order_length < 3:
            order = input("what else? ")
            if order in menu:
                order_list.append(order)
                order_length += 1
                if order_length == 2:
                    promt = False
            else:
                print("That is not in the menu, I'm sorry. Please try again. ")
    else:
        print("That is not in a menu, I'm sorry. Please try again. ")

print(f"You have chosen {order_list[0]}, {order_list[1]} and {order_list[2]}")
