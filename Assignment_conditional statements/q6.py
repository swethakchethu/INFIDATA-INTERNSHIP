day=int(input("enter the number form 1 to 7"))
if day==1:
    print("sunday")
if day == 2:
    print("monday")
if day == 3:
    print("tuesday")
if day == 4:
    print("wednesday")
if day == 5:
    print("thursday")
if day == 6:
    print("friday")
if day == 7:
    print("saturday")
    present=int(input("enter the total number of working days"))
absent=int(input("enter the total number absent days"))
per=(present-absent)/present*100
print("class attended",per)
if per<75:
    print("you will not able to sit in exam")
else:
    print("you will be able to attend the exam")