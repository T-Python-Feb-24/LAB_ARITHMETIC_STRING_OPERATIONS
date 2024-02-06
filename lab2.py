#Defining a variable named "price" and setting its value to the cost of the item.
price:float = 14.99

#Defining a variable named "quantity" and setting its value to the number of items.
quantity:float = 7

#Defining a variable named "tax_rate" and set its value to the tax rate 15%
tax_rate:float = 0.15

#Calculate the subtotal
subtotal:float = round(price*quantity, 2)

#Calculate the tax
tax:float = round(subtotal*tax_rate, 2)

#Calculate the total cost
total:float = round(tax + subtotal, 2)

#Print the subtotal, tax, and total costs
print('```')
print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print("Tax rate: 15%")
print()
print(f'Subtotal: ${subtotal}')
print(f'Tax: ${tax}')
print(f'Total: ${total}')
print('```')
