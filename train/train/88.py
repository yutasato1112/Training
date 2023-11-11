import random
ram=random.randint(1,99)
n=1
while True:
    
    num_user=int(input("please input number"))
    if num_user<ram:
        print("This number is smaller than the computer number.")
        n=n+1
    elif num_user>ram:
        print("This number is bigger than the computer number.")
        n=n+1
    else:
        print("correct! you takes "+str(n)+" times.")
        break
        


