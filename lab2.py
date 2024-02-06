# Prices of items
Apple = 9.99
Ice_cream = 12.75
water = 1.65
Monga = 11.20

# Quantity of items being purchased
quantity = 4

# Tax rate (converted to decimal for calculation)
tax_rate = 7.5 / 100

# Calculate the subtotal by multiplying the price by the quantity for each item and summing them up
subtotal = (Apple + Ice_cream + water + Monga) * quantity

# Calculate the tax by multiplying the subtotal by the tax rate
tax = subtotal * tax_rate

# Calculate the total cost by adding the subtotal and the tax
total = subtotal + tax

# Print the subtotal, tax, and total costs, formatted as currency
print(f"Price of Apple: ${Apple:.2f}")
print(f"Price of Ice Cream: ${Ice_cream:.2f}")
print(f"Price of Water: ${water:.2f}")
print(f"Price of Monga: ${Monga:.2f}")
print(f"Quantity of items: {quantity}")
print(f"Tax Rate:{tax_rate} %")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Tax: ${tax:,.2f}")
print(f"Total: ${total:,.2f}")



