x = 25
y = 645
z = 341
if(x%2 == 0 or y%2 == 0 or z%2==0):
    if (x > y and x % 2 == 0):
        print(x, "is odd and the largest")
    elif(x > z and x % 2 == 0):
        print(x,"is odd and the largest")
    elif(y > x and y % 2 == 0):
        print(y,"is odd and the largest")
    elif(y > z and y % 2 == 0):
        print(y,"is odd and the largest")
    elif(z > x and z % 2 == 0):
        print(z,"is odd and the largest")
    elif(z > y and z % 2 == 0):
        print(z,"is odd and the largest")
else:
    print("No odds")
