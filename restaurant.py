# restaurant waiter helper program
menu = ["chicken soup", "roast duck with rice", "special fried rice", "pizza", "chips", "burger"]
print("In our menu, we have {}, {}, {}, {}, {} and {}".format(menu[0], menu[1], menu[2], menu[3], menu[4], menu[5]))
order_list = []
order = input("What would you like to order? ")
order_list.append(order)
order = input("And? ")
order_list.append(order)
order = input("And? ")
order_list.append(order)
print(f"You have chosen {order_list[0]}, {order_list[1]} and {order_list[2]}")