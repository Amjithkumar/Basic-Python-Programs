mat1=[]
mat2=[]
amat=[]
r=int(input("Enter the no .of row"))
c=int(input("Enter the no.of columns"))
print("Enter the elements in matrix 1")
for i in range(r):
    row=[]
    for j in range(c):
        ele=int(input())
        row.append(ele)
    mat1.append(row)
print("Matrice 1 is :",mat1)
print("Enter the elements in matrix 2")
for i in range(r):
    row=[]
    for j in range(c):
        ele=int(input())
        row.append(ele)
    mat2.append(row)
print("Matrice 2 is",mat2)
print("Sum of the 2 matrices is : \n")
for i in range(r):
    for j in range(c):
        row=[]
        ele=mat1[i][j]+mat2[i][j]
        row.append(ele)
    amat.append(row)
print("sum of matrices :",amat)
