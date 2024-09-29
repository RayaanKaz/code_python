#quadrant select
xCoord = int(input("Enter in x coordinate: "))
yCoord = int(input("Enter in y coordinate: "))

if xCoord > 0 and yCoord > 0:
    print("Quadrant 1")

elif xCoord < 0 and yCoord > 0:
    print("Quadrant 2")

elif xCoord < 0 and yCoord < 0:
    print("Quadrant 3")

else:
    print("Quadrant 4")