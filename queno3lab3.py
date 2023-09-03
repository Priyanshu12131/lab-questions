d1=int(input("Enter the side1: "))
d2=int(input("Enter the side2: "))
d3=int(input("Enter the side3: "))
if d1<0 or d2<0 or d3<0:
    print("Enter a valid side")
if (d1+d2>d3 or d1+d3>d2 or d2+d3>d1) and (d1>0 or d2>0 or d3>0):
    print("All three sides form triangle ")
else:
    print("Not a triangle")