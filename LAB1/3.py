v1= [1,0,2,0,3]
v2= [1,2,0,3,1]


ok=0
if(len(v1)<len(v2)):
    ok=1

s=0
if(ok==0):
    for i in range(0,len(v2)):
        s=s+abs(v1[i])*abs(v2[i])
    
print(s)