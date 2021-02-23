mat = [[0,0,0,1,1],
 [0,1,1,1,1],
 [0,0,1,1,1]]


sumMax=0
index=0
imax=-1
for i in mat:
    if(sumMax<sum(i)):
        sumMax=sum(i)
        imax=index
    index+=1

print(sumMax)
print(imax)