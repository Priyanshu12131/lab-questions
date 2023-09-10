n=int(input("inter a number:"))
temp=n
re=0
while(n>0):
    dig=n%10
    re=(re*10)+dig
    n=n//10
if(temp==re):
   print("the number is palindrome!")
else:
    print("the number is not palindrome!")