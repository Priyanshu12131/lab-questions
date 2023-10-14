x=int(input())
f=(x//100)
s=(x%100)//10
t=(x%10)
c=(f+s+t)
if x%3==0:
    print('divisible by 3')
else:
    print('not divisible by 3')
