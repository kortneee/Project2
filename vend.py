#MSC260 Fall 2020 Project 2
#Kortnee Reiss
#Declaration: I, Kortnee Reiss, am the sole author of this code, which
#was developed in accordance with the rules in the course syllabus. 
import sys
def read_inventory(fn): 
    """Reads fn, if the command is inventory, returns the list inventory, in the order: index, name,
    price, and number available. If fn is the index, the price of the item will return """
    global inventory
    inventory = [{"name": "Cheesy dibbles", "stock": 6, "price": 125},
    {"name": "Oat biscuits", "stock": 10, "price": 115},
    {"name": "Sugar rings", "stock": 12, "price": 75},
    {"name": "Celery crunchies", "stock": 5, "price": 150},
    {"name": "Astringent persimmon", "stock": 6, "price": 205},
    {"name": "Almond crescents", "stock": 10, "price": 95}]
    if fn =="inventory":
        for i in range(len(inventory)):
            print(i, inventory[i]['name'], '${:,.2f}'.format(float(inventory[i]['price'])/100), "("+str(inventory[i]['stock']),"available)")
    elif (int(fn)<6):
        return(float(inventory[int(fn)]['price'])/100)
def dispense_change(cents):
    while cents>0:
        if cents>=0.25:
            cents=cents-0.25
            print("RETURN: quarter")
        elif (cents>=0.10):
             cents=cents-0.10
             print("RETURN: dime")
        elif (cents >=0.05):
            cents=cents-0.05
            print("RETURN: nickel")
    cents=credit
credit = 0.00
highprice = 2.05
while (credit >= 0.00 and credit<=highprice):
    print("CREDIT:",'${:,.2f}'.format(credit))
    task = input()
    if (task =="inventory"):
        print(read_inventory(task))
    elif task == "quarter":
        if (credit +0.25)>highprice:
            print("RETURN: quarter")
        credit=credit + 0.25
    elif task == "dime":
        if (credit +0.10)>highprice:
            print("RETURN: dime")
        credit=credit + 0.10
    elif task == "nickel":
        if (credit +0.05)>highprice:
            print("RETURN: nickel")
        credit=credit + 0.05
    elif (int(task)<=5):
        if (credit < read_inventory(task)):
            print("MSG: Insufficient credit")
        elif(inventory[int(task)]['stock']>=0):
            credit= credit-read_inventory(task)
            inventory[int(task)]['stock'] = (inventory[int(task)]['stock'])-1
            print("VEND:", inventory[int(task)]['name'])
            print(dispense_change(credit))
    elif(task=="exit"):
        break
    elif(task=='restock'):

