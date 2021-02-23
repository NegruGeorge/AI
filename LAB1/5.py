map={}

v=[1,2,3,4,2]

for i in v:
    if(i not in map):
        map[i] = 0
    
    map[i]+=1

for i in map:
    if(map[i]!=1):
        print(str(i) + " se repeta de " + str(map[i]) )


