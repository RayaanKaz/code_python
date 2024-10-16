def stringDuplicates(string1, string2):
    repeatList = []
    for char in string1:
        if char in string2:
            repeatList.append(char)
    
    return sorted(repeatList)


firstString = input("Enter in your first string: ")
secondString = input("Enter in your second string: ")

print(stringDuplicates(firstString, secondString))

