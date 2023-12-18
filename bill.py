from datetime import datetime

name = input("Enter your name: ")
items_list = '''
Rice   Rs 40/kg
Oil    Rs 140/liter
Sugar  RS 30/kg
Salt   Rs 15/kg
Paneer Rs 140/kg
Boost  Rs 90/each
Colgate Rs 30/each
'''

# Declaration
totalprice = 0
finalamount = 0
ilist = []
qlist = []
plist = []

# Rates for items
items = {'rice': 40, 'oil': 140, 'sugar': 30, 'salt': 15, 'paneer': 140, 'boost': 90, 'colgate': 30}
option = int(input('For the list of items, press 1: '))
if option == 1:
    print(items_list)

pricelist = []  # List to store individual item prices

for i in range(len(items)):
    inp1 = int(input("If you want to buy, press 1 or 2 for exit: "))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your items: ")
        quantity = int(input("Enter quantity: "))
        if item in items.keys():
            # Calculate price for the current item
            price = quantity * items[item]
            totalprice += price  # Accumulate the total price

            # Add item details to the lists
            pricelist.append((item, quantity, items[item], price))
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)

        else:
            print("Sorry, your item is not available")
    else:
        print("You entered the wrong number")

# Check if the user wants to proceed with billing
inp = input("Can I bill the items? (yes or no): ")
if inp.lower() == 'yes' and totalprice != 0:
    print(25 * "=", "Victory Supermarket", 25 * "=")
    print(28 * " ", "Madanapali")
    print("Name:", name, 30 * " ", "Date:", datetime.now())
    print(75 * "-")
    print("Sno", 8 * " ", 'Items', 8 * " ", 'Quantity', 3 * " ", 'Price')
    for i in range(len(pricelist)):
        print(i, 8 * ' ', 5 * ' ', ilist[i], 3 * ' ', qlist[i], 8 * " ", plist[i])
    print(75 * "-")
    print(50 * " ", 'Total Amount:', 'Rs', totalprice)

    # Calculate GST and final amount
    gst = (totalprice * 5) / 100
    finalamount = gst + totalprice
    
    print("GST amount", 50 * " ", 'Rs', gst)
    print(75 * "-")
    print(50 * " ", 'Final Amount:', 'Rs', finalamount)
    print(75 * "-")
    print(20 * " ", "Thanks for visiting")
    print(75 * "-")
