#Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
price = 2.99


#Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).
quantity = 3
print("Quantity: ", quantity)

#Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).
tax_rate = 7.5
print("Tax rate: %",tax_rate)

#Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal".
subtotal = price * quantity
print("Without tax: ", subtotal)

#Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".
tax = subtotal * 0.075
print("Tax: ", tax)

#Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".
total = subtotal + tax 
print("The total is: ", total)

