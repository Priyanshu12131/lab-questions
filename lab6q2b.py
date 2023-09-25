n=int(input("enter the number of terms:"))
fact=1
sum=0
a=1
for i in range(1,n+1):
    fact=fact*i
    sum+=1/fact
    a+=1
print(f"the no of the series for {n} terms is approximately {sum:.9f}")