l = int (input("enter length"))
b = int (input("enter breadth"))
h = int (input("enter height"))

while (True):
    choice = int (input("enter ypur choice 1:area , 2:volume, 3: exit"))
    if (choice ==1):
        area = l*b
        print("area of the rectangele is :",area)
    elif (choice ==2):
        vol = l*b*h
        print("vol of the rectangle is :",vol)
    elif(choice==3):
        exit(0)
    else:
        print("invalid choice")