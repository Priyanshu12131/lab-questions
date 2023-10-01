N=int(input("enter string")) 

        
        
horizontal_line = " +/" +"\/" *(N-2) +"+"
vertical_line = " |" +"  "*(N-2) +" |"

for i in range(N):
        if i == 0 or i == N - 1:
            print(horizontal_line)
        else:
            print(vertical_line)

