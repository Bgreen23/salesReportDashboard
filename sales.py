import matplotlib.pyplot as plt
import numpy as np

results = []
id = []
salesperson = []
make = []
model = []
year = []
vin = []
base_price = []
accessories = []
taxes = []
date = []

with open("sales.json") as salesFile:
    reader = json.reader(salesFile, quoting=json.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader:
        id.append(row[0])
        salesperson.append(int(row[1]))
        make.append(int(row[2]))
        model.append(int(row[3]))
        year.append(int(row[4]))
        vin.append(int(row[5]))
        base_price.append(int(row[6]))
        accessories.append(int(row[7]))
        taxes.append(int(row[8]))
        date.append(int(row[9]))
