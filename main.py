import colorama
from colorama import init
from colorama import Fore, Style
init()

#Todo: Drop item-->Item Database-->Validate Item Existence-->Player basics-->???

#Error Codes:
#1 - Couldnt add item for some reason,figure it out 


print("Inventory System 0.0.1 by: github.com/trkviktor")
msg = "slot is full"
items = ["Sword", "Axe"]


inventorySlot1 = ["Sword"]
inventorySlot2 = ["armor"]
inventorySlot3 = ["axe"]
inventorySlot4 = ["axe"]
inventory = [inventorySlot1, inventorySlot2, inventorySlot3,inventorySlot4]



def addItem(name, slot):
    slot.append(name)
    print(slot[0])


def getInventory():

    if inventorySlot1:
        print("Slot 1: " + inventorySlot1[0])
    else: print("Slot 1: empty")

    if inventorySlot2:
        print("Slot 2: " + inventorySlot2[0])
    else: print("Slot 2: empty")

    if inventorySlot3:
        print("Slot 3: " + inventorySlot3[0])
    else: print("Slot 3: empty")

    if inventorySlot4:
        print("Slot 4: " + inventorySlot4[0])
    else: print("Slot 4: empty")

    print("----------\n")
    print(inventory)
    print("\n----------\n")


name = input("Enter your items name:")

if not inventorySlot1:
    slot = inventorySlot1
    addItem(name, slot)
elif not inventorySlot2 :
    slot = inventorySlot2
    addItem(name, slot)
elif not inventorySlot3:
    slot = inventorySlot3
    addItem(name, slot)
elif not inventorySlot4:
    slot = inventorySlot4
    addItem(name, slot)
elif inventory:
    print("\n" + Fore.RED + "Inventory is full")
    print(Style.RESET_ALL)
else:
    print("\n" + Fore.RED + "Something went wrong-beep boop error code: 1")
    print(Style.RESET_ALL)
    
   
getInventory()
    

