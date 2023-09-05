a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if a==0:
    print("Enter the coefficient correctly")
else:
    disc=b*b-4*a*c
if disc>0:
    print("Real and diff roots")
    print((-b+disc)/2)
    print((-b-disc)/2)
elif disc==0:
    print("real and equal roots")
    print(-b/(2*a))
else:
    print("Complex roots exist")
