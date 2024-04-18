a1 = int(input("enter the num1:"))
b2 = int(input("enter the num2:"))
choice=int(input("enter your choice 1:add,2:sub,3:mul,4:div,5:per"))

if (choice == 1):
        res = a1 + b2
        print("add of{0} and {1} is {2}".format(1, 2, res))
elif (choice == 2):
        res = 1 - 2
        print("sub of {0} and {1} is {2}".format(1, 2, res))
elif (choice == 3):
        res = 1 * 2
        print("mul of {0} and {1} is {2}".format(1, 2, res))
elif (choice == 4):
        res = 1 / 2
        print("div2"" of {0} and {1} is {2}".format(1, 2, res))
elif (choice == 5):
        res = 1 % 2
        print("per of {0} and {1} is {2}".format(1, 2, res))
else:
        print("invalid choice")


