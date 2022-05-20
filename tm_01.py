def countEvenOdd(x):
    even = 0
    odd = 0
    t = n
    while(t > 0):
        m = t % 10
        if(m % 2 == 0):
            even += 1
        else:
            odd += 1
        t = t // 10
    print(f"\ncount even : {even}")
    print(f"count odd  : {odd}")
# 
# 
n = int(input("input number : "))
countEvenOdd(n)