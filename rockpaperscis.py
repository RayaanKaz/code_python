#create rock paper scissors game

first = input('''Player One
A. Rock
B. Paper
C. Scissors
''')
second = input('''Player Two
A. Rock
B. Paper
C. Scissors
''')
if first == second:
    print("tie")
else:
    if first == 'A':
        if second == 'B':
            print("Player two won")
        else:
            print("Player one won")
    elif first == 'B':
        if second == 'C':
            print("Player Two won")
        else:
            print("Player one won")
    else:
        if second == 'A':
            print("Player Two won")
        else:
            print("Player one won")
        
#sigma park hi