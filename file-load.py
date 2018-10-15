import json

with open('sales_staff.json', 'r') as staffFile:
    obj = json.loads(staffFile.read())
    print(obj)
