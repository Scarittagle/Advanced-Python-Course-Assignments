#Homework 2 
#WEIWEI SU
#U17420699
#Last Modified Date: 09/02/2017

def displayInventory(Inventory):
    print("Inventory: ")
    for key,value in Inventory.items():
        print(str(value) + ' ' + key)
    print("Total number of Items: " + str(sum(Inventory.values())))

def addToInventory(Inventory, addedItems):
    for item in addedItems:
        Inventory[item] = Inventory.get(item, 0) + 1
    return Inventory
