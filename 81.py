lists=[]
lists=(input("please input 3 number:").split())
for i in range(len(lists)):
    lists[i]=int(lists[i])
lists.sort()
print(lists[1])
