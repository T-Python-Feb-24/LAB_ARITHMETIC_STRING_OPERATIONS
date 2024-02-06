# Define a variable named "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).
price:float =2.99
#Define a variable named "quantity" and set its value to the number of items the customer is purchasing (e.g., 3).
quantity:int=3
#Define a variable named "tax_rate" and set its value to the tax rate in your area (e.g., 7.5%).
tax_rate:float=0.075
'''
Calculate the subtotal by multiplying the price by the quantity 
and store the result in a variable named "subtotal".
'''
subtotal=round(price*quantity,2)
#Calculate the tax by multiplying the subtotal by the tax rate (in decimal form, e.g., 0.075) and store the result in a variable named "tax".
tax=round(subtotal*tax_rate,2)
#Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".
total=round(tax+subtotal,2)
#Print the subtotal, tax, and total costs, formatted as currency (e.g., $8.97 for the total cost).
print("Price of item: $"+str(price))
print("Quantity: "+str(quantity))
print("Tax rate: 7.5%")
print()
print("Subtotal: $"+str(subtotal))
print("Tax: $"+str(tax)+"$")
print("Total: $"+str(total))

'''
The output is: 
Price of item: $2.99
Quantity: 3
Tax rate: 7.5%

Subtotal: $8.97
Tax: $0.67$
Total: $9.64
'''