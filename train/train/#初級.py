#First
"""
#No.20
a=int(input("please 1st:"))
b=int(input("please 2st:"))
c=a//b
print("result 1:  "+str(c))
print("result 2:  "+str(c*b))

#21
a=int(input("please number"))
if 5<a<20:
    print("OK")

#22
a=int(input("please number: "))

#Using abs is scary...

if a<=-10 or a>=10:  
    print("OK")


#23
a=int(input("please number: "))

if -5<=a<10:
    print("OK")
else:
    print("NG")

#24
a=int(input("please number: "))
if -10<=a<0 or a>=10:
    print("OK")
else:
    print("NG")

#25
a=int(input("please number: "))
if a<-10:
    print("range 1")
elif -10<=a<0:
    print("range 2")
elif a>=0:
    print("range 3")

#26
#Cant use syntax"switch". Can use match
num=input("please number: ")
match num:
    case "1":
        print("one")
    case "2":
        print("two")
    case "3":
        print("three")
    case _:
        print("other")
# cant solve


#27
a=int(input("please number: "))
if a>0:
    lists=list(range(a+1))
    print("sum :"+str(sum(lists)))
else:
    print("sum :"+"0")

#28
a=int(input("please number: "))
b=1#unknown
for i in range(a,1,-1):
    b=b*i
print(b)
#review

#29

lists=[0]
for i in range(5):
    a=int(input("please number: "))
    lists_a=lists.append(a)
    print(lists_a)
#unknown


#30
a=int(input("please number: "))
if a>0:
    print("*"*a)
else:
    print("")


#31
a=int(input("please number: "))
if a>0:
    b=a//5
    c=a%5
    print("***** "*b+"*"*c)
else:
    print("")

#32
for i in range(1,21):
    if i%5 == 0:
        print("bar")
    else:
       print(i)

#33
a=int(input("please number: "))
for i in range(1,10):
    if i !=a:
       print(i)
#review


#34
a=int(input("please number: "))
for i in range(1,10):
    if i !=a and i !=a+1:
       print(i)
    elif a==9:
        print(i)
"""
#35
a=[3,7,0,8,4,1,9,6,5,2]
#unknown






































