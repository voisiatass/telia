from datetime import datetime
import random

f = open("file.txt", "a")

#How many random orders
y = random.randint(10, 20)
for j in range(0, y):
	#how many orderitems
	x = random.randint(0,19)
	for i in range(0,x):
		itemId = random.randint(0, 100)
		orderId = j
		qty = random.randint(0, 5)
		price = "{:.2f}".format(random.uniform(0.01, 20.00))
		date = "01-02-2020"
		data = [itemId, orderId, qty, price, date]
		f.write(str(itemId))
		f.write(", ")
		f.write(str(orderId))
		f.write(", ")
		f.write(str(qty))
		f.write(", ")
		f.write(str(price))
		f.write(", ")
		f.write(str(date))
		f.write(", ")
		f.write("\n")

f.close()

with open("file.txt") as file_in:
    wholeList = []
    for line in file_in:
    	lines = []
        lst = line.split(',')
        lines.append(lst[0])
        lines.append(lst[1])
        lines.append(lst[2])
        lines.append(lst[3])
        lines.append(lst[4])
        wholeList.append(lines)
    print(wholeList[1])



