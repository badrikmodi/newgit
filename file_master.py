import json

with open('orgs.json', 'r') as fp:
    obj = json.load(fp)
    print(obj,'obj')
    print('---------------------')
    print(type(obj),'---type----')
    x = obj[0]
    print(x,'x')


print("otherchanges addition")

print("2nd change by otherchanges addition")
