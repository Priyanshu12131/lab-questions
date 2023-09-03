a=int(input("basic sallary:"))
hra=0.2*a
ta=0.5*a
da=0.1*a
gs=hra+ta+da+a
print(gs)
if gs<300000:
    print("the income tax:0 % gs")
if gs>300000:
    print("the income tax:10%gs")
if gs>1000000:
    print("the income tax:20%gs")
if gs>2500000:
    print("the income tax:30%GS")
