n = int(input("enter (length of list of integers):"))
l=list()
sum = 0 
product = 1

for i in range(n):
    l.append(int(input("enter a integer: ")))

for a in (l):
    sum = sum + a
for b in (l):
    product=product*b


print(f"the list of the integers {l}")
print(f"the sum of the elements of the list is {sum}")

print(f"the product of the elements of the list is product {product}")
a=l[0]
m=a
for d in l:
    if d>a:
     m=d
print(m)