# 1. Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
# 2. Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).
# 3. Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).
# 4. Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal".
# 5. Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".
# 6. Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".

price:float = 5.80
quantity:int = 3 
tax_rate:float = 15.0
subtotal:float = price * quantity
tax:float = round(subtotal * (tax_rate/100),2)
total:float = round(subtotal + tax,2) 

# 7. Print the subtotal, tax, and total costs, formatted as currency (e.g., $8.97 for the total cost).
print(f'''Subtotal: ${subtotal}
      \n Tax: ${tax}
      \n Total: ${total}''')
 
# Addison Step To check all the values: 
print(f'''Price of item: ${price}
      \n Quantity: {quantity} 
      \n Tax rate: {tax_rate}%
      \n Subtotal: ${subtotal}
      \n Tax: ${tax}
      \n Total: ${total}''')

