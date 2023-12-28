l=int(input("Enter the lower limit :"))
u=int(input("Enter the upper limit :"))
for i in range(l,u+1):
    if(i==1):
        print(i,"Number is not a composite or prime\n prime numbers are  :")
        continue
    for j in range(2,i):
        if(i%j==0):
            break
    else:
             print(i)
