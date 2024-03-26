from datetime import datetime


subtotal = -1
price = 0
quantity = 0
end = False

def item_add():
    quantity = int(input("How many items?  "))
    price = float(input("What is the price of each item? "))
    line_price = quantity * price
    return line_price

today = datetime.now()
weekday = int(today.weekday())

while end == False:
    
    subtotal += item_add()
    again = input("Do you have more to add? Y or N: ")
    if again.upper() == "Y":
        end = False
    else:
        end = True

if weekday == 1 or weekday == 2:
    if subtotal < 50:
        print(f"You missed out on our promotion. You were ${(50 - subtotal):.2f} away from qualifying for a discount!")
    else:
        discount = subtotal *.1
        print(f"Congratulations, you qualified for our discount! Your new total is ${(subtotal - discount):.2f}. Have a great day! ")
else:
    print(f"Your total comes to ${subtotal:.2f}.")