n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
l=list()
l2=list()
l3=list()


for i in range(n1):
    l.append(int(input("enter a integer: ")))

for j in range(n2):
    l2.append(int(input("Enter elements: ")))

set_a=l
set_b=l2


for k in range(0,n1+1):
            if (k in  l) and (k  in l2):
                l3.append(k)
print(set(l3))