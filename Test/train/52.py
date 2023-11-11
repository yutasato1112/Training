year=int(input("please enter year"))
if year%4==0:
    if year%100!=0 or year%400==0:
        print(str(year)+"uru year")
    else:
        print(str(year)+"not uru year")
else:
        print(str(year)+"not uru year")

