import json
from collections import defaultdict
d=defaultdict(int)
def createInventory():
    k=[]
    n=int(input("how many types of products you want"))
    for i in range(n):
        d={}
        d["id"]=int(input("enter the id of your product"))
        d["name"]=input("enter name of the product")
        d["price"]=input("enter the price of the product")
        d["quantity"]=input("enter the quantity present in the inventory")
        k.append(d)
    with open("ch.json", "w") as f:
        json.dump(k, f)


def addItem():
    k=defaultdict()
    a=[]
    n=int(input("enter how many items you need to add"))
    for i in range(n):
        with open("ch.json", "r") as f:
            d = json.load(f)
        k["id"]=int(input("enter the id of your product"))
        k["name"]=input("enter name of the product")
        k["price"]=input("enter the price of the product")
        k["quantity"]=input("enter the quantity present in the inventory")
        d.append(k)
        with open("ch.json", "w") as f:
            json.dump(d, f)


def load():
    with open("ch.json", "r") as f:
        d = json.load(f)
        return d
    
def total_value():
    count=0
    with open("ch.json", "r") as f:
        d = json.load(f)
    for i in d:
        count+=int(i["quantity"])*int(i["price"])
    print(count)


def delItem():
    k=int(input("enter the id of the product you want to delete from inventory"))
    with open("ch.json", "r") as f:
        d = json.load(f)
    for i in d:
        if i["id"]==k:
            d.remove(i)
    with open("ch.json", "w") as f:
        json.dump(d, f)
    

def search():
    with open("ch.json", "r") as f:
        d = json.load(f)
    print(d)
    k=int(input("enter the id of the item which you want to search"))
    for i in d:
        if i["id"]==k:
            return i
    return "not found"
def updateDetails():
    try:
        a=int(input("enter the id of the item which you wanted to change"))
        k=input("enter the attribute name you want to change")
        v=input("enter the value to be changed")
        with open("ch.json", "r") as f:
            d = json.load(f)
        for i in d:
            if i["id"]==a:
                i[k]=v
        with open("ch.json", "w") as f:
            json.dump(d, f)
        print("update sucessfull")
        
            
    except:
        print("enter correct data")





