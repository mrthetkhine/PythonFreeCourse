price = 12.3
quantity = 3
total = price * quantity
print("price is {} quantity {} total {}".format(price,quantity,total))
print("quanity is {1} price {0} total {2}".format(price,quantity,total))
print("quanity is {qty} price {price} total {total}".format(qty=quantity,total=total,price=price))

print("Quantity is :{:d}".format(quantity))
print("Quantity is :{:5d}".format(quantity))
print("Quantity is :{:05d}".format(quantity))

print("Total is :{:f}".format(total))
print("Total is :{:.2f}".format(total))
print("Total is :{:7.2f}".format(total))
print("Total is :{:07.2f}".format(total))

print("Quantity in binary is :{:b}".format(quantity))
print("Quantity in ocatal is :{:o}".format(quantity))
print("Quantity in hexa is :{:x}".format(quantity))

print("{:5d}".format(18))
print("{:<5d}".format(18))
print("{:>5d}".format(18))
