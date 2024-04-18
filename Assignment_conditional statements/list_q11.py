l1=[]
for i in range (6):
    num= int (input("enter a num to the list"))
    l1.append(num)
    print("elements \t \t frequency")
    for i in l1:
        print(i,end ="\t")
        print(l1.count(i))