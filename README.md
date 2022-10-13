# Restaurant Waiter Helper Program
In this exercise, we will learn on how to print out a list inside a human-readable string.
<br/> For this instance, inside a restaurant, we want to give the customer a list of manu in a format for them to understand what is available in the manu.
First lets start with the list:
```python
menu = ["chicken soup", "roast duck with rice", "special fried rice", "pizza", "chips", "burger"]
```
The we need to print this to the customer so it can understand in a readable way. 
```python
print("In our menu, we have {}, {}, {}, {}, {} and {}".format(menu[0], menu[1], menu[2], menu[3], menu[4], menu[5]))
```
We then need to be able to take in the orders the customer will want. Therefore, we will want an empty list. We will then need to ask the customer what they will like and add this to the empty list, we can use the `append()` function.
```python
order_list = []
order = input("What would you like to order? ")
order_list.append(order)
order = input("And? ")
order_list.append(order)
order = input("And? ")
order_list.append(order)
```
As the final task, we will then output the list so that the customer knows what was ordered for no confusion.
```python
print(f"You have chosen {order_list[0]}, {order_list[1]} and {order_list[2]}")
```
