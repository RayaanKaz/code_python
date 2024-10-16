import math

def mean(givenList):
    total = 0
    for num in givenList:
        total += num
    
    average = total / ((len(givenList)))

    return average

def median(givenList):
    totalNums = len(givenList)
    givenList = sorted(givenList)
    if totalNums % 2 == 0:
        middle1 = (totalNums / 2)
        middle2 = (totalNums / 2) - 1
        average2 = (totalNums[middle1] + totalNums[middle2]) / 2
        
        return average2

    else:
        median = math.floor((totalNums / 2))

        return (givenList[median])


givenList = [1,5,6,2,3,14,11]

print(mean(givenList))
print(median(givenList))