v = [2,8,7,2,2,5,2,3,1,2,2]
n = len(v)

map ={}

for i in v:
    if(i not in map):
        map[i]=0
    map[i]+=1

for i in map:
    if(map[i]> n/2):
        print(str(i) + " e majoritar")

