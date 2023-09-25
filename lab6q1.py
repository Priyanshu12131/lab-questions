a=input("enter a sentences:")
vowel_count=0
cons_count=0
word_count=1
for char in a:
    if (char=='a'or char=='e' or char=='i'or char=='o'or char=='u'or char=='A'
       or char=='E'or char=='I'or char=='O'or char=='U'):
      vowel_count+=1
    elif char!=" " and char!="\t" and char!="\n":
            cons_count+=1
    elif char==" ":
         word_count+=1
print("total vowel=",vowel_count)
print("total cons=",cons_count)
print("total word",word_count)