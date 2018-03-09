#Gregory Clarke
#Computer Programming
#2/28/2018

def new_inventory():
    inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217} #the dictionary 'inventory'
    item=inventory[input("What item do you need to change?: ")]
    remove=int(input("How many would you like to remove?: "))
    newitem=item-remove #subracts 'remove' from 'item'
    print("You now have "+str(newitem)) #prints the difference

new_inventory()
