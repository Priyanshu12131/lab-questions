a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
d=(b**2)-(4*a*c)
if a==0:
    print("equation is invalid")
if d<0:
    print("imagenery roots")
elif d==0:
    print("real and equal roots")
    Y=((-b/(2*a)))
    print(Y)
elif d>0:
    print("real and distinct roots")
    X1=((-b+(d**0.5)/(2*a)))
    X2=((-b(-d**0.5)/(2*a)))
    print("the roots are:",X1,X2)
