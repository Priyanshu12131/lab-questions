s=str(input("Enter any paragraph:"))
d_count=0
alpha_count1=0
alpha_count2=0
s_count=0
for char in s:
    if char.islower():
        alpha_count1+=1
    elif char.isupper():
        alpha_count2+=1
    elif char.isdigit():
        d_count+=1
    else:
        s_count+=1
print("the lower characters count is:",alpha_count1)
print("the upper characters count is:",alpha_count2)
print("the digit count is:",d_count)
print("the special character count is:",s_count)