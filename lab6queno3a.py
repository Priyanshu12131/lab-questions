N=int(input("enter a number:"))
a=1
sum=0
for i in range(0,N):
    sum=sum+(1/2)**a
    a+=1
    print(f"{sum:.9f}")