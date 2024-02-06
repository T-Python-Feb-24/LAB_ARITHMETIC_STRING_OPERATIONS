price: float = 2.99
quantity: int = 3
tax_rate: float = 7.5/100

subtotal: float = price * quantity
tax: float = subtotal * tax_rate
total: float = subtotal + tax

print(f'''
Price of item: ${price}
Quantity: ${quantity}
Tax Rate: {tax_rate:0.1%}

Subtotal: ${subtotal}
Tax: ${tax:.2f}
Total: ${total:.2f}
''')
