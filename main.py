import colorama
from colorama import init
from colorama import Fore, Style
init()

openMenu = True

#Todo: Player basics-->???

#Error Codes:
#1 - Couldnt add item for some reason,figure it out 


print(Fore.GREEN + "Inventory System 0.0.1 by: github.com/trkviktor\n")
print(Style.RESET_ALL)
msg = "slot is full"


axes = ["Diamond Axe", "Iron Axe"]
armors = ["Steel Armor", "Leather Armor"]
swords = ["Wooden Sword", "Gold Sword"]

itemDB = [axes,armors,swords]

items = []
for i in itemDB:
    items.extend(i)



print(items)




inventorySlot1 = []
inventorySlot2 = []
inventorySlot3 = []
inventorySlot4 = []
inventory = [inventorySlot1, inventorySlot2, inventorySlot3,inventorySlot4]




    


def addItem(name, slot):
    if not inventorySlot1:
        slot = inventorySlot1
        slot.append(name)
    elif not inventorySlot2 :
        slot = inventorySlot2
        slot.append(name)
    elif not inventorySlot3:
        slot = inventorySlot3
        slot.append(name)
    elif not inventorySlot4:
        slot = inventorySlot4
        slot.append(name)
    elif inventory:
        print("\n" + Fore.RED + "Inventory is full")
        print(Style.RESET_ALL)
    else:
        print("\n" + Fore.RED + "Something went wrong-beep boop error code: 1")
        print(Style.RESET_ALL)
        
    
def deleteItem(slot):
    removeSlotName = input("\n\nEnter your desired slot(1-4): ")
    if removeSlotName == "1":
        slot = inventorySlot1
    elif removeSlotName == "2":
        slot = inventorySlot2
    elif removeSlotName == "3":
        slot = inventorySlot3
    elif removeSlotName == "4":
        slot = inventorySlot4
    else:
        print("\n\nEnter a valid slot!")
    

    slot.clear()


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


def Menu():
    while True:
            print("\nEnter your desired menu option:")
            menuInput = input("Options: Inventory,Additem,Removeitem,Exit :\n\n")
            if menuInput == "Inventory":
                getInventory()
            elif menuInput == "inventory":
                getInventory()
            elif menuInput == "Additem":
                name = input("Enter your items name:")
                if name in items:
                     addItem(name, inventorySlot4)
                     print("\n\n" + name + " Added")
                else:
                     print("\n\nItem does not exist")
            elif menuInput == "additem":
                name = input("Enter your items name:")
                if name in items:
                     addItem(name, inventorySlot4)
                     print("\n\n" + name + " Added")
                else:
                     print("\n\nItem does not exist")
            elif menuInput == "Removeitem":
                deleteItem(inventorySlot4)
            elif menuInput == "removeitem":
                deleteItem(inventorySlot4)
            elif menuInput == "Exit":
                break
            elif menuInput == "exit":
                break
            else:
                continue


if openMenu:
    Menu()
