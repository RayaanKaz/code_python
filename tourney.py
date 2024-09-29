#tourney stuff hi mr park if you are reading for some reason
counter = 0
games = 0

while games < 6:
    result = input("Enter w or l: ")
    games += 1
    if result == 'w':
        counter += 1

group = 0
if counter == 1 or counter == 2:
    group += 3
if counter == 3 or counter == 4:
    group += 2
if counter == 5 or counter == 6:
    group += 1

print(f"You are in group {group}")
