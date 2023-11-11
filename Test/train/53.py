num = int(input("please number"))
n=2
while True:
    if num%n==0:
        num=num/n
        print(n)
    else:
        n=n+1
    if num<n:
        break
