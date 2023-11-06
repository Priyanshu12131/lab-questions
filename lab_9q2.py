n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
l=list()
l2=list()


for i in range(n1):
    l.append(int(input("enter a integer: ")))

for j in range(n2):
    l2.append(int(input("Enter elements: ")))

set_a=set(l)
set_b=set(l2)
print(set_a and set_b)