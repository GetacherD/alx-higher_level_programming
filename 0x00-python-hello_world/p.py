d = 0
b = [[2, 3], [6, 7], [8, 9]]
b = [[b[j][i] for j in range(len(b))] for i in range(len(b[0]))]
a =[ [1, 2, 1] ,[2 , 1, 2], [2, 2, 2]]
e =[]
f = []
for row in range(len(a)):
    for col in range(len(b)):
        for x, y in zip(a[row], b[col]):
            d += x * y
        e.append(d)
        d = 0
    f.append(e)
    e =[]
    print()
print(f)
     
