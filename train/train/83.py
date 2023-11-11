import random
import time
lists=[]
a=str(input("please your hands"))
ram=str(random.randint(0,2))
print("computer enter..."+ram)
lists.append(a)
lists.append(ram)

for i in range(2):
    lists[i]=int(lists[i])
a=int(a)
ram=int(ram)

for i in range(3,0,-1):
    print(i)
    time.sleep(1)

if a>2:
    print("cannot take number")
elif ram==a:
    print("same")
elif lists==[0,1] or lists==[1,2] or lists==[2,0]:
    print("you win.")
else:
    print("you are baka")

