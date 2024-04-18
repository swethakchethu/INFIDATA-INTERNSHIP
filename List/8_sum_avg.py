l1=[1,2,3,4,5,15,4]
sum=0
avg=0
for i in l1:
    sum=sum+i
    print("sum of all elements of l1 is:",sum)
    avg=sum/len(l1)
    print("avg of l1 is:",avg)

    for i in l1[:3]:
        print(i)

