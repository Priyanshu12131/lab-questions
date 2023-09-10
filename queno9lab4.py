H=input("enter a sentence: ")
upp=0
lower=0
dig=0
spec=0
ind=0
while ind<len(H):
  char=H[ind]
  if'A'<=char<='Z':
    upp+=1
  elif 'a'<=char<='z':
    lower+=1
  elif '0'<=char<='9':
    dig+=1
  else:
    spec+=1
  ind+=1
print(upp)
print(lower)
print(dig)
print(spec)
