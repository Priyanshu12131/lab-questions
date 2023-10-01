sen = str(input('enter a sentence: '))
sen =sen.lower()
sen= sen.replace(' ','')
a =''
for i in sen:
    if i not in a:
        a= a+i
a = a.replace('',' ')
a = a.split()
a.sort()
print(a)

l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
if a==l:
    print('pangram')
else:
    print('not a pangram')