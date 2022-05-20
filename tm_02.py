while(1):
    print("Enter the number of the problem you wish to slove.")
    print("GIVEN A MEDICAL ORDER IN CALCULATOR RATE IN")
    print("(1) ml/hr& tubing drop factor drops / min")
    print("(2) 1 L for n hr ml / hr")
    print("(3) mg/kg/hr& concentration in mg/ml ml / hr")
    print("(4) units/hr& concentration in units/ml ml / hr")
    print("(5) QUIT")
    n = int(input("Problem > "))
    if(n == 1):
        r = int(input("Enter rate in ml/hr > "))
        t = int(input("Enter tubing's drop factor(drops/ml) > "))
        res = (r * t) // 60
        print(f"The drop rate per minute is {res}")
    elif(n == 2):
        r = int(input("Enter number of hours > "))
        b = 15.625
        res = r * b
        print(f"The rate in milliliters per hour is {res}.")
    elif(n == 3):
        a = int(input("Enter rate in mg / kg / hr   > "))
        b = int(input("Enter patient weight in kg   > "))
        c = int(input("Enter concentration in mg/ml > "))
        res = a * b * c
        print(f"The rate in milliliters per hour is {res}.")
    elif(n == 4):
        a = int(input("Enter rate in units / hr > "))
        b = int(input("Enter concentration in units / ml > "))
        res = a // b
        print(f"The rate in milliliters per hour is {res}.")
    elif(n == 5):
        break
    else:
        print("input number between 1 .. 5")