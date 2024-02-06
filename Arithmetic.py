 # 1. Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
price = 2.99
print(f"Price of item: ${price}")

# 2. Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).
quantity = 3
print(f"Quantity of items: {quantity}")

# 3. Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).
tax_rate = f"{0.075:.1%}"
print("Tax rate: ", tax_rate ,'\n')

# 4. Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal".
subtotal = price * quantity
#print(f"Subtotal: ${subtotal}")

# 5. Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".
tax_dec = float(tax_rate.strip('%')) / 100
tax = round(subtotal * tax_dec, 2)
#print(f"Tax: ${tax}")

# 6. Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".
total = subtotal + tax
#print(f"Total: ${total}")

# 7. Print the subtotal, tax, and total costs, formatted as currency (e.g., $8.97 for the total cost).
print(f'Subtotal: ${subtotal}\nTax: ${tax}\nTotal Cost: ${total}')