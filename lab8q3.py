n = int(input("enter a no of elements:"))
list1=[]
for i in range(n):
    element=float(input("enter the value:"))
    list1.append(element)
for i in range(n):
    for j in range (0,n-i-1):
        if list1[j]>list1[j+1]:
             list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)
