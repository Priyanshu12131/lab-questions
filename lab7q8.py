a=str(input("enter a sentence:"))
b=str(input("enter any word:"))
a=a.split()
l=len(a)
b_count=0
for i in range(0,1):
    if b in a[i]:
        b_count+=1
print(b_count)