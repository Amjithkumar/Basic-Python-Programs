def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
def exp(a,b):
    return(a**b)
def main():
    x=int(input("Enter the first number :"))
    y=int(input("Enter the second number :"))
    s=int(input("\n 1.FOR ADDITION \n 2.FOR SUBSTRACTION \n 3.FOR MULTIPLICATION \n 4.FOR DIVISION \n 5.FOR EXPONENT"))
    if(s==1):
        print("sum=",add(x,y))
    elif(s==2):
        print("difference=",sub(x,y))
    elif(s==3):
        print("product=",mul(x,y))
    elif(s==4):
        if(y==0):
            print("DIVISION BY ZERO IS NOT POSSIBLE")
        else:
            print("division=",div(x,y))
    elif(s==5):
        print("power=",epx(x,y))
    else:
        print("invalid entry")
    c=int(input("Want to continue press 1 \n 0 to exit"))
    if(c==1):
        main()
main() 
