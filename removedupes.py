def removeDupes(stringList):
    newList = []

    for char in stringList:
        if char not in newList:
            newList.append(char)
    
    return newList

test = ['a','b','c','e','e','a','d','f','g']

print(removeDupes(test))
