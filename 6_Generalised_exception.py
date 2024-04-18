n1=int (input("enter a first num:"))
n2=int(input("enter a second num:"))
l1=[4,5,6,7,8]
print("l1 is:",l1)
try:
    div=n1/n2
    print("red of div:",div)
    print("l1[2]:",l1[2])
    print("l1[5]:",l1[5])
except ZeroDivisionError as e:
    print(" u r trying to divide an int num by zero")
    print("e value:",e)
except Exception as e:
    print("am at Gernalised except block")
    print("e value:",e)

print("end")