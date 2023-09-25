x=float(input("enter the value of x:"))
n=int(input("enter the number of terms:"))
sum=0
a=1

for i in range(1,n+1):
    term=(x**i)/i
    sum+=term
    a+=1
print(f"the no of the series for {n} terms is approximately {sum:.9f}")