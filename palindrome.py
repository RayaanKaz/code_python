def isPalindrome(word):
    # Emptiness is equal it false which is why not
    if not word: # a more efficient version of if len(word) == 0:
        return True
    # one char
    elif len(word) == 1:
        return True
    # Base case is two or 3 chars
    elif len(word) <= 3:
        # middle doesnt matter if 2 or 3 chars and first and last value or the same
        # will return true or false
        return word[0] == word[-1]
    else:
        #Solution 1 compare if the reversed version is equal to the original
        flipped = word[::-1] # to reverse a slicable obj in python (identity) 
        return flipped == word

        #Solution2 compare first half and last half

        #Solution 3 start at front and back and start comparing
        i = 0
        j = len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            
            i += 1
            j -= 1
        # end of while loop
        return True

userInput = isPalindrome(input("Enter string buddy: "))

if userInput == True:
    print("Hurrah")
else:
    print("Boo")