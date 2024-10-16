def cleanString (clean):

    result = ''
    for char in word:
        if char.isalpha():
            result += char.lower()
    
    return result

value = cleanString(input("Enter a string"))

print(f"Cleaned version: {value}")