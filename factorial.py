
def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

if __name__ == "__main__":
    num = input("what do you want the factorial of?  ")
    print("the factorial of " , num , "is", factorial(int(num)))
