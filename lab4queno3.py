#taking input
n=int(input("enter a number:"))
#initialization variable
sum=0
#condition
while n!= 0 :
  sum=sum+(n%10)
  n=n//10
  ##printing the sum of digits
print("sum of digits is",sum)
