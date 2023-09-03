num=input("enter number:")
sum=0
for i in num:
    sum+=int(i)**3
if sum==int(num):
    print('armstrong')
else:
    print('not armstrong')