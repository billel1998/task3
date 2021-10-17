def printmat(a):
    i = 0
    j = 0
    for i in range(a[i][j]):
        for j in range(a[i][j]):
            print(a)
    return a
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the number of rows: ")

for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
matrix = printmat(matrix)









