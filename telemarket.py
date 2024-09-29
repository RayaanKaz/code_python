# Telemarketer code fun stuff hey mr park how are you im listening to bruno mars right now
line1 = int(input("Input number 0-9: "))
line2 = int(input("Input number 0-9: "))
line3 = int(input("Input number 0-9: "))
line4 = int(input("Input number 0-9: "))

telemarketer = False

if line1 == 8 and line1 == 9 and line4 == 8 and line4 == 9 and line2 == line3:
    telemarketer = True

if telemarketer == True:
    print("Ignore")
else:
    print("Answer")
    
