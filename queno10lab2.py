number = 70000 #int(input("enter number between1 to 86400"))
second = number%60
hours = number//3600
minutes = int(abs(hours-(number/3600))*60)
print(hours,minutes,second)