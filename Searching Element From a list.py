list=[]
e=int(input("Enter the number of elements in the list"))
print("Enter the elements in the list")
for i in range(0,e):
    ele=int(input())
    list.append(ele)
for i in list:
    print(i)
x=int(input("Enter the element to  start search"))
f=0
c=1
for i in list:
    if(x==i):
        print(x,"is in the list at pos",c)
        f=1
        break
    c=c+1
if(f==0):
    print("Element is not in the list")
