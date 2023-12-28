def fact(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    elif(n>0):
         return n*fact(n-1)
n=int(input("Enter the value of n"))  
r=int(input("Enter he value of r"))
ncr=fact(n)/(fact(n-r)*fact(r))
print(n,"C",r,"=",ncr)
        
