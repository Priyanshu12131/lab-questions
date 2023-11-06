n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
l=list()
l2=list()


for i in range(n1):
    l.append(int(input("enter a integer: ")))

for j in range(n2):
    l2.append(int(input("Enter elements: ")))

set_a=l
set_b=l2

print("union: ",set_a or set_b)
print("intersection: ",set_a and set_b)
print("symmetric difference: ",((set_a-set_b) and (set_b-set_a)))

