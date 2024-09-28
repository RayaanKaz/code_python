from math import ceil


firstFence = input("Input the amount of fences in the first row with F's: ")
secondFence = input("Input the amount of fences in the second row with F's: ")
thirdFence = input("Input the amount of fences in the third row with F's: ")

firstLength = len(firstFence)
secondLength = len(secondFence)
thirdLength = len(thirdFence)

sum = firstLength + secondLength + thirdLength

boxesofPaint = ceil(sum/12)
leftover = 12*boxesofPaint - sum

print(sum)
print(leftover)
print((boxesofPaint*14.95))