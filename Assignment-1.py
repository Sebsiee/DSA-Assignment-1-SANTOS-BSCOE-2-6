letter_S = [[" " for i in range(5)] for j in range(7)]
letter_E = [[" " for i in range(5)] for j in range(7)]
letter_B = [[" " for i in range(5)] for j in range(7)]

for row in range(7):
    for col in range(5):
        if ((row==0 or row==3 or row==6) and (col>0 and col<4)) or (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
            letter_S[row][col] ="*"

for row in range(7):
    for col in range(5):
        if col==0 or ((row==0 or row==3 or row==6) and (col>0)):
            letter_E[row][col] ="*"

for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
            letter_B[row][col] ="*"

for i in range(7):
    for j in range(5):
        print(letter_S[i][j], end=" ")
    print(end="  ")
    for j in range(5):
        print(letter_E[i][j], end=" ")
    print(end="  ")
    for j in range(5):
        print(letter_B[i][j], end=" ")
    print(end="  ")
    print()