#special day code my birthday is october 11 btw anyone reading this
month = int(input("Enter in a number 1-12: "))
day = int(input("Enter a number 1-30: "))

if ((month > 2) or (month == 2 and day > 18)):
    print("After")
elif ((month < 2) or (month == 2 and day < 18)):
    print("Before")
else:
    print("Special")