price:float = 4.6
print(f"price of item: ${price}")
quantity: int = 33
print(f"Quantity:{quantity}")
tax_rate: float= 0.065
print(f"tax Rate:{tax_rate}%")
subtotal = (price*quantity)
tax:float = (subtotal*tax_rate)
total = (subtotal+tax)
sub1= f"subtotal:${subtotal}"
print(sub1)
tax1= f"tax:${tax}"
print(tax1)
tot1=f"total:${total}"
print(tot1)





