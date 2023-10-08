n = int(input("enter (length of list of integers):"))
l=list()


for i in range(n):
    l.append(int(input("enter a integer: ")))
l2=[]
for j in range(0,n):
    s=min(l)
    l2.append(s)
    l.remove(s)
print(l2)