a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
c=input("enter the operation you wish to perform among '+' , '-' , 'x' , '/' : ")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="x":
    print(a*b)
elif c=="/":
    print(a/b)
else :
    print ("invalid operator")