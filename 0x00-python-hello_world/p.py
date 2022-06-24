d = 0
b = [[3, 4], [5, 6]]
# b = [[b[j][i] for j in range(len(b))] for i in range(len(b[0]))]
a = [[1, 4,2]]
e =[]
f = []
for row in range(len(a)):
    for col in range(len(b[0])):
        for k in range(len(a[row])):
            d += a[row][k] * b[k][col]
        e.append(d)
        d = 0
    f.append(e)
    e =[]
    print()
print(f)
     
