def factorsCounter(factors):
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    return counter

number = int(input("Enter a number (integer) to count the factors for: "))

numberOf = factorsCounter(number)

print(f"The number of factors for {number} is {numberOf}")