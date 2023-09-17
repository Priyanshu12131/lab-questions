num=int(input("enter a number:"))
divisible_count=0
indivisible_count=0
n=int(input("enter a number:"))
while num!=-999:
    if n%num==0:
        divisible_count=divisible_count+1
    else:
        indivisible_count=indivisible_count+1
    num=int(input("entter a number:"))
print("The divisible count is:",divisible_count)
print("The indivisible count is:",indivisible_count)