mat =[[0,2,5,4,1],
      [4,8,2,3,7],
      [6,3,4,6,2],
      [7,3,1,8,3],
      [1,5,7,9,4]]

print(mat)

p1 = (2,2)
p2 = (4,4)


s=0
for i in range(1,4):
    for j in range(1,4):
        s+=mat[i][j]

print(s)