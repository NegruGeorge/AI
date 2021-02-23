v = "Ana are mere rosii si galbene"

v = v.lower()
print(v)
s = v.split()
print(s)


poz = 0
last = s[0]

for i in s:
    if(i[0]> last[0]):
        last = i
      

print(last)

