n=int(input("enter number:"))
i=1
fact=1
if n<0:
    print("eror")
if n==0:
    print("factorial is 1") 
while i<=n:
        fact=fact*i
        i=i+1
print(fact)