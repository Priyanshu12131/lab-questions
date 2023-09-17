N=int(input("enter a positive number between 1-20:"))
if 1<=N<=20:
 i=1
 while i<=N:
    print(f"multiplication tables for{i}:")
    j=1
    while j<=20:
        result=i*j
        print(f"{i}X{j}={result}")
        j+=1
    i+=1    
else:
    print("please enter a positive integer between 1-20.")