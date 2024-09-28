firstName = input("What is your first name: ")
lastName = input("What is your last name: ")
year = int(input("What is your birth year: "))

print(f"{firstName} {lastName}")
age = 2024 - year
print(f"You are {age} years old")
if age < 18:
    print("You are not old enough to drink")
else:
    print("You can drink")