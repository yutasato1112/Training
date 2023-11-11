import random
lists_1=[]

times = int(input("please count times"))
for i in range(times):
    ran=str(random.randint(1,6))
    lists_1.append(ran)
listts_1_i=[int(j) for j in lists_1]

print(sum(listts_1_i))

