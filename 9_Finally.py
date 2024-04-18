l1=[1,2,3,4]
print("l1 is:",l1)
try:
    print("l1[2]:",l1[2])
    print("l1[5]:",l1[5])
except ZeroDivisionError as e:
    print("an at zeroDivisionError except block")
    print("e value:",e)
finally:
    print("am at finally block:")
    print("execution at finally")
print("end")
    
