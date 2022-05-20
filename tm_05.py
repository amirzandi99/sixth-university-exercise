while(1):
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplaction")
    print("4 Division")
    print("5 Factorial")
    print("6 QUIT\n")
    n = int(input("Enter the choice : "))
    if(n == 1):
        num1 = int(input("Enter number 1 : "))
        num2 = int(input("Enter number 2 : "))
        r = num1 + num2
        print(f"sum : {r}\n\n")
    elif(n == 2):
        num1 = int(input("Enter number 1 : "))
        num2 = int(input("Enter number 2 : "))
        r = num1 - num2
        print(f"Submission : {r}\n\n")
    elif(n == 3):
        num1 = int(input("Enter number 1 : "))
        num2 = int(input("Enter number 2 : "))
        r = num1 * num2
        print(f"Multiplication : {r}\n\n")
    elif(n == 4):
        num1 = int(input("Enter number 1 : "))
        num2 = int(input("Enter number 2 : "))
        if(num2 != 0):
            r = num1 // num2
            print(f"Division : {r}\n\n")
        else:
            print("error for zero\n\n")
    elif(n == 5):
        num1 = int(input("Enter number 1 : "))
        f = 1
        for i in range(1,num1+1):
            f *= i
        print(f"factorial : {f}\n\n")
    elif(n == 6):
        break
    else:
        print("Enter number between 1 .. 5 !\n\n")