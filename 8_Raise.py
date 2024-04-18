print(" raise keyword demo")
try:
    raise ZeroDivisionError ("demo message")
except ZeroDivisionError as e:
    print("an at zeroDivisionError except block")
    print("e value:",e)
print("end")