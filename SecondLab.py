#You are a cashier at a grocery store. Write a Python program to calculate the total cost of a customer's purchase, including tax.

#Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
price = 2.99

print(f"price of item: $ {price}")
      
#Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).
quantity = 3

print(f"quantity: { quantity}")
#Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).
tax_rate = 7.5/100

print(f"tax_rate: % { tax_rate }")
#Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal".
subtotal = price * quantity

print(f"subtotal:$ {subtotal}")
#Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".
tax = subtotal * tax_rate

print(f"tax:$ {tax:.2f}")
#Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".
total = subtotal + tax 

print(f"total: {total:.2f}")
#Print the subtotal, tax, and total costs, formatted as currency (e.g., $8.97 for the total cost).