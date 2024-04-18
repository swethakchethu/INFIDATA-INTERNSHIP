print("select a food category 1: veg, 2: non_veg")
choice = int (input())
if (choice == 1):
    print("you have selected veg category")
    menu = int(input("select memu 1: meals 2: idly 3: dosa"))
    if (menu ==1):
        print("you have selected meals")
    elif (menu ==2):
        print("you have selected idli")
    elif (menu ==3):
        print("you have selected dosa")
    else:
        print ("menu not available")
elif (choice ==2):
    print("you have selected non_veg")
    menu = int (input("select menu 1:biryani 2: chicken"))
    if (menu==1):
        print("you have selected biryani")
    elif (menu ==2):
        print("you have selected chicken")
else:
    print("invalid category")