a=[[100,89,93,72,19],[67,78,45,89,23],[24,87,89,17,49],[45,72,83,16,94],[87,37,94,27,84]]
jap=[]
mat=[]
sce=[]
soc=[]
eng=[]
for i in a:
    jap.append(i[0])
    mat.append(i[1])
    sce.append(i[2])
    soc.append(i[3])
    eng.append(i[4])
jap.sort()
mat.sort()
sce.sort()
soc.sort()
eng.sort()
js=sum(jap)
ms=sum(mat)
ss1=sum(sce)
ss2=sum(soc)
es=sum(eng)
jap_t=js/(len(jap))
mat_t=ms/(len(mat))
sce_t=ss1/(len(sce))
soc_t=ss2/(len(soc))
eng_t=es/(len(eng))
jc=jap[2]
mc=mat[2]
sc1=sce[2]
sc2=soc[2]
ec=eng[2]
print("Avaragesocore of Japnanese :"+str(jap_t)+" median score :"+str(jc))
print("Avaragesocore of Math :"+str(mat_t)+" median score :"+str(mc))
print("Avaragesocore of Scence :"+str(sce_t)+" median score :"+str(sc1))
print("Avaragesocore of Social Study :"+str(soc_t)+" median score :"+str(sc2))
print("Avaragesocore of English :"+str(eng_t)+" median score :"+str(ec))
bls=["A","B","C","D","E"]
for i in range(len(a)):
    suma=sum(a[i])
    name=bls[i]
    print(str(name)+"'s sum score :"+str(suma))
    