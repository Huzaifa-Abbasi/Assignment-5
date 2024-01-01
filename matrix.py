a = [[1, 2],[3, 4]]
b = [[5, 6],[7, 8]]

for i in a,b:
    print(i)


for i in range(1):
    for j in range(1):
        c=a[i][j]+b[i][j]
        print("the sum of matrix=",c)
print()        