start = float(input("How much money did we have before selling cookies: "))

cookies = input("Enter c's to represent cookies sold: ")

bigcookie = input("Enter big b's to represent big cookies sold: ")

counter = 0
money = start

for character in cookies:
    if character == 'c':
        counter += 1
        money += 0.75

for character in bigcookie:
    if character == 'b':
        counter += 1
        money += 1.25

print(f"Number of cookies sold: {counter}")
print(f"Money made: ${money}")
