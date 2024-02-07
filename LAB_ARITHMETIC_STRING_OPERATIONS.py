# Point 1
price = float(input("Enter The Item Price -> "))
# Point 2
quantity = int(input("Enter The Item Quantity -> "))
# Point 3
tax_rate = float(input("Enter The Tax percentage -> "))
tax_rate = tax_rate/100
# Point 4
SubTotal = quantity * price
# Point 5
tax = round (SubTotal*tax_rate,3)
# Point 6
total = round (SubTotal + tax,2)
# Point 7
print(f"The Price -> ${price}")
print(f"The Quantity -> {quantity}")
print(f"Tax Rate 15% -> {tax_rate}")
print(f"Subtotal -> ${SubTotal}")
print(f"Tax -> ${tax}")
print(f"Total -> ${total}")