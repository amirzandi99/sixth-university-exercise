while(1):
    print("(1) Area of a parallelogram")
    print("(2) Area of a triangle")
    print("(3) Area of a trapezoid")
    print("(4) Area of a circle")
    print("(5) QUIT\n")
    n = int(input("input number : "))
    if(n == 1):
        base = int(input("input base   : "))
        height = int(input("input height : "))
        r = base * height
        print(f"result : {r}\n\n")
    elif(n == 2):
        base = int(input("input base   : "))
        height = int(input("input height : "))
        r = base * height / 2
        print(f"result : {r}\n\n")
    elif(n == 3):
        base1 = int(input("input base 1 : "))
        base2 = int(input("input base 2 : "))
        height = int(input("input height : "))
        r = (base1 + base2 / 2) * height
        print(f"result : {r}\n\n")
    elif(n == 4):
        Pi = 3.14
        radius = int(input("input radius : "))
        r = Pi * (radius * radius)
        print(f"result : {r}\n\n")
    elif(n == 5):
        break
    else:
        print("input number between 1 .. 5 !\n\n")