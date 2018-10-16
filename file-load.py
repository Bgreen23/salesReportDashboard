import json

with open('sales_staff.json', 'r') as staffFile:
    obj = json.loads(staffFile.read())
    print(obj)

with open('sales.json','r') as salesFile:
    obj = json.loads(salesFile.read())
    print(obj)
