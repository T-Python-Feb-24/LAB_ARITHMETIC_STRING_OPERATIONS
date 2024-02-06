# 1. The cost of the item the customer is purchasing "$"
price:float = 2.99
# 2. The number of items the customer is purchasing
quantity:int = 3
# 3. The tax rate in your area "%"
tax_rate:float = 7.5

# 4. Calculate the subtotal "$"
subtotal = price * quantity

# 5. Calculate the tax "$"
tax = subtotal * (tax_rate/100)

# 6. Calculate the total cost "$"
total = subtotal + tax

#7.1 print the define variables
print("Price of item: ${}".format(price))
print("Quantity: {}".format(quantity))
print("Tax rate: {}%".format(tax_rate))
print("\n")

#7.2 print the results of calculations
print("Subtotal: ${}".format(subtotal))
print("Tax: ${}".format(round(tax, 2)))
print("total: ${} ".format(round(total, 2)))


