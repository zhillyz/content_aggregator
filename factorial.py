def factorial(value):
    """gives the factorial of the value"""
    fac = 1
    for i in range(1,value+1):
        fac *= i
    print(fac)

factorial(4)