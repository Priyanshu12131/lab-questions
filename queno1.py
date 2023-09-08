N=int(input("enter a number:"))
if N<0:
    ("invalid input,plese enter positive integers")
elif N>0:
    count=1
    while count<21:
        print(N,"x",count,"=",N*count)
        count+=1
