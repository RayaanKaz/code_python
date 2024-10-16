def checkCons(wordSet):
    counter = 0
    for char in wordSet:
        char = char.lower()
        if char.isalpha() and char not in {'a', 'e', 'i', 'o', 'u'}:
            counter += 1
        
    return counter


wordSet = checkCons(input("Enter in a word to check: "))

print(f"# of consonants is: {wordSet}")


