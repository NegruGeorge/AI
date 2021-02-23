map ={}
text = "ana are ana are  mere rosii ana"
v = text.split()

for i in v:
    if(i not in map):
        map[i]=0
    map[i]+=1

print(map)

for i in map:
    if(map[i]==1):
        print(i)