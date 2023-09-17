N=int(input("enter a positive number:"))
if N<=0:
    print("plese enter a positive number.")
else:
    i=1
    while i<=1000:
        if i%N==0:
            i+=1
            continue
        print(i, end=' ')
        i +=1