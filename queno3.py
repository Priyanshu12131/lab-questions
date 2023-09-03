x=int(input("Enter 1: "))
y=int(input("enter 2: "))
if x<=0 and y<=0:
    print("invalid input")
    
if y%x==0:
    print("y is divisible by x")
else:
    print("no")