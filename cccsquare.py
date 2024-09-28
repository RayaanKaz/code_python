from math import sqrt, floor

squares = int(input("How many squares does Gigi have? "))
answer = sqrt(squares)
answer = floor(answer)

print(f"The maxium side length is {answer}")

