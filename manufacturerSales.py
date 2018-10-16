import json
import matplotlib.pyplot as plt
import numpy as np
sales = None

with open('sales.json','r') as salesFile:
    sales = json.loads(salesFile.read())

for i in range(len(sales)):
    print(sales[i]['make'])


make = {}

for i in range(len(sales)):
    names = sales[i]['make']
    if names in make:
        make[names] += 1
    else:
        make[names] = 1

print(make)

plt.rcdefaults()
fig, ax = plt.subplots()

manufacturer = (make.keys())
totalSales = (list(make.values()))
y_pos = range(len(make))

ax.barh(y_pos, totalSales, color = "green")
plt.yticks(range(len(make)), list(make.keys()))
ax.set_xlabel('Units Sold')
ax.set_title('Units Sold Per Manufacturer')

plt.show()
