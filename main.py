price_of_itme :float  = 3.75 
Quantity : int = 5
tax_rate :float = 5.3



subtotal = price_of_itme * Quantity
Tax = subtotal * 0.053
total = subtotal + Tax 


output1 = "Price of item : ${} \n Quantity : {} \n Tax rate : {} % \n".format(price_of_itme , Quantity , tax_rate)
output2 = "\n Subtotal : ${} \n Tax : ${:.2f} \n Total : ${:.2f} ".format(subtotal,Tax , total)

print(output1 , output2)
