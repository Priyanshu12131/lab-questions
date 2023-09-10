num=int(input("enter a number:"))
f=0
i=2
if num<0:
    print ("invalid input")
if num==1:
        print("1 is neither prime or nor composite:")
while i<num/2:
    if num%i==0:
        f=1
        break
        i=i+1
if f==0:
     print("the entered number is prime number")
else:
    print("the entered number is not  prime number")
        


