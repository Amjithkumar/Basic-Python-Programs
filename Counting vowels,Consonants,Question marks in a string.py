str=input("Enter the sring")
w=len(str.split())-1
q=len(str.split('?'))-1
v=0
h=0
for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        v=v+1
    if(i.isalpha()==True):
        h=h+1
c=h-v
print("\n Number of vowels",v)
print("\nNumber of consonants",c)
print("\nNumber of words",w)
print("\n Number of ? marks",q)
