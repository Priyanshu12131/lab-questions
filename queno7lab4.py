n=int(input("enter value:"))
x=1
y=1
sum=x+y
count=1
print("fab0nacci series is:")
while(count<=n):
    count+=1
    print(x)
    x=y
    y=sum
    sum=x+y