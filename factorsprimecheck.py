def functionPrime(bigNum):
    count = 1
    factors = 0
    while count <= bigNum:
        if bigNum % count == 0:
            factors += 1
        count += 1

    if factors == 2:
        return True
    else:
        return False
    

num = functionPrime(int(input("Enter in a number for the factors: ")))

print(f"Is it prime: {num}")