def stringPattern(number):
    pattern = ''
    for i in range (1, (number + 1)):
        if i % 2 != 0:
            pattern += '1'
        else:
            pattern += '0'

        
        print(pattern)


v = stringPattern(int(input("Enter in an integer: ")))