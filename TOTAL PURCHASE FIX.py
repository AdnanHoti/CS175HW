item1 = float(input("enter the price of item 1: "))
item2 = float(input("enter the price of item 2: "))
item3 = float(input("enter the price of item 3: "))
item4 = float(input("enter the price of item 4: "))
item5 = float(input("enter the price of item 5: "))
subtotal = item1+item2+item3+item4+item5
tax = subtotal*7/100
total = subtotal+tax

print("Candy",format(item1,"10,.2f"))
print("Eggs",format(item2,"10,.2f"))
print("Milk",format(item3,"10,.2f"))
print("Cereal",format(item4,"10,.2f"))
print("Bread",format(item5,"10,.2f"))
print("Subtotal ",format(subtotal,"10,.2f"))
print("Tax7% ",format(tax,"10,.2f"))
print("Total ",format(total,"10,.2f"))
