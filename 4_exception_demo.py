n1=int (input("enter a first num:"))
n2=int(input("enter a second num:"))
try:
    div=n1/n2
    print("result of div:",div)
except ZeroDivisionError as e:
    print("u r typing to divide on int num by zero")
    print("e value:",e)
print("end")    